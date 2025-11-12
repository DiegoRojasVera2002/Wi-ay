from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
import enum

class UserRole(str, enum.Enum):
    STUDENT = "student"
    COMPANY = "company"
    ADMIN = "admin"

class DifficultyLevel(str, enum.Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.STUDENT)
    university = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    enrollments = relationship("Enrollment", back_populates="student")
    submissions = relationship("Submission", back_populates="student")

class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    category = Column(String)  # "Data Science", "IoT", "Web Dev"
    icon = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    projects = relationship("Project", back_populates="module")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    module_id = Column(Integer, ForeignKey("modules.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    company_name = Column(String, nullable=False)
    difficulty = Column(Enum(DifficultyLevel))
    order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    module = relationship("Module", back_populates="projects")
    steps = relationship("Step", back_populates="project")
    enrollments = relationship("Enrollment", back_populates="project")

class Step(Base):
    __tablename__ = "steps"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    content = Column(Text)  # Guía, videos, recursos
    test_input = Column(Text)  # JSON con casos de prueba
    test_output = Column(Text)  # JSON con outputs esperados
    order = Column(Integer, default=0)

    # Relationships
    project = relationship("Project", back_populates="steps")
    submissions = relationship("Submission", back_populates="step")

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    progress = Column(Integer, default=0)  # Porcentaje 0-100
    completed = Column(Boolean, default=False)
    enrolled_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

    # Relationships
    student = relationship("User", back_populates="enrollments")
    project = relationship("Project", back_populates="enrollments")

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    step_id = Column(Integer, ForeignKey("steps.id"))
    code = Column(Text, nullable=False)
    language = Column(String, default="python")
    status = Column(String)  # "pending", "passed", "failed"
    test_results = Column(Text)  # JSON con resultados
    submitted_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    student = relationship("User", back_populates="submissions")
    step = relationship("Step", back_populates="submissions")

class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    certificate_url = Column(String)
    issued_at = Column(DateTime, default=datetime.utcnow)
