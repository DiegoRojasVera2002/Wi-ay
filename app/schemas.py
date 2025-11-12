from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    university: Optional[str] = None

class UserCreate(UserBase):
    password: str
    role: str = "student"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: int
    role: str
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    user: User

# Module Schemas
class ModuleBase(BaseModel):
    title: str
    description: str
    category: str
    icon: Optional[str] = None

class ModuleCreate(ModuleBase):
    pass

class Module(ModuleBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Project Schemas
class ProjectBase(BaseModel):
    title: str
    description: str
    company_name: str
    difficulty: str
    order: int = 0

class ProjectCreate(ProjectBase):
    module_id: int

class Project(ProjectBase):
    id: int
    module_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Step Schemas
class StepBase(BaseModel):
    title: str
    description: str
    content: str
    test_input: Optional[str] = None
    test_output: Optional[str] = None
    order: int = 0

class StepCreate(StepBase):
    project_id: int

class Step(StepBase):
    id: int
    project_id: int

    class Config:
        from_attributes = True

# Submission Schemas
class SubmissionCreate(BaseModel):
    step_id: int
    code: str
    language: str = "python"

class Submission(BaseModel):
    id: int
    student_id: int
    step_id: int
    code: str
    language: str
    status: str
    test_results: Optional[str] = None
    submitted_at: datetime

    class Config:
        from_attributes = True

# Enrollment Schemas
class EnrollmentCreate(BaseModel):
    project_id: int

class Enrollment(BaseModel):
    id: int
    student_id: int
    project_id: int
    progress: int
    completed: bool
    enrolled_at: datetime

    class Config:
        from_attributes = True
