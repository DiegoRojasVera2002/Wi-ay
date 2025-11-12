from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import Project as ProjectModel, Step as StepModel, Enrollment as EnrollmentModel
from ..schemas import Project, ProjectCreate, Step, Enrollment, EnrollmentCreate

router = APIRouter()

@router.get("/{project_id}", response_model=Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return project

@router.get("/{project_id}/steps", response_model=List[Step])
def get_project_steps(project_id: int, db: Session = Depends(get_db)):
    steps = db.query(StepModel).filter(
        StepModel.project_id == project_id
    ).order_by(StepModel.order).all()
    return steps

@router.post("/enroll", response_model=Enrollment)
def enroll_in_project(enrollment: EnrollmentCreate, user_id: int, db: Session = Depends(get_db)):
    # Check if already enrolled
    existing = db.query(EnrollmentModel).filter(
        EnrollmentModel.student_id == user_id,
        EnrollmentModel.project_id == enrollment.project_id
    ).first()

    if existing:
        return existing

    # Create enrollment
    db_enrollment = EnrollmentModel(
        student_id=user_id,
        project_id=enrollment.project_id
    )
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment
