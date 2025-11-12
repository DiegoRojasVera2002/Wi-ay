from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json
import subprocess
import tempfile
import os

from ..database import get_db
from ..models import Submission as SubmissionModel, Step as StepModel
from ..schemas import Submission, SubmissionCreate

router = APIRouter()

def test_code(code: str, test_input: str, test_output: str) -> dict:
    """
    Simple code testing - runs Python code with test inputs
    """
    try:
        test_cases = json.loads(test_input) if test_input else []
        expected_outputs = json.loads(test_output) if test_output else []

        results = []
        passed = 0

        for i, (test_case, expected) in enumerate(zip(test_cases, expected_outputs)):
            # Create temp file with code
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                # Add test case as input
                full_code = f"{code}\n\nresult = solution({json.dumps(test_case)})\nprint(result)"
                f.write(full_code)
                temp_file = f.name

            try:
                # Run code
                result = subprocess.run(
                    ['python3', temp_file],
                    capture_output=True,
                    text=True,
                    timeout=5
                )

                output = result.stdout.strip()

                # Check if output matches expected
                if output == str(expected):
                    results.append({"test": i+1, "status": "passed"})
                    passed += 1
                else:
                    results.append({
                        "test": i+1,
                        "status": "failed",
                        "expected": expected,
                        "got": output
                    })
            except subprocess.TimeoutExpired:
                results.append({"test": i+1, "status": "timeout"})
            except Exception as e:
                results.append({"test": i+1, "status": "error", "message": str(e)})
            finally:
                os.unlink(temp_file)

        return {
            "passed": passed,
            "total": len(test_cases),
            "results": results,
            "status": "passed" if passed == len(test_cases) else "failed"
        }
    except Exception as e:
        return {
            "passed": 0,
            "total": 0,
            "results": [],
            "status": "error",
            "error": str(e)
        }

@router.post("/submit", response_model=Submission)
def submit_code(submission: SubmissionCreate, user_id: int, db: Session = Depends(get_db)):
    # Get step to get test cases
    step = db.query(StepModel).filter(StepModel.id == submission.step_id).first()
    if not step:
        raise HTTPException(status_code=404, detail="Paso no encontrado")

    # Test the code
    test_results = test_code(submission.code, step.test_input, step.test_output)

    # Save submission
    db_submission = SubmissionModel(
        student_id=user_id,
        step_id=submission.step_id,
        code=submission.code,
        language=submission.language,
        status=test_results["status"],
        test_results=json.dumps(test_results)
    )
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)

    return db_submission

@router.get("/step/{step_id}", response_model=list[Submission])
def get_submissions(step_id: int, user_id: int, db: Session = Depends(get_db)):
    submissions = db.query(SubmissionModel).filter(
        SubmissionModel.step_id == step_id,
        SubmissionModel.student_id == user_id
    ).order_by(SubmissionModel.submitted_at.desc()).all()
    return submissions
