from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import Module as ModuleModel, Project as ProjectModel
from ..schemas import Module, ModuleCreate, Project

router = APIRouter()

@router.get("/", response_model=List[Module])
def get_modules(db: Session = Depends(get_db)):
    modules = db.query(ModuleModel).all()
    return modules

@router.get("/{module_id}", response_model=Module)
def get_module(module_id: int, db: Session = Depends(get_db)):
    module = db.query(ModuleModel).filter(ModuleModel.id == module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Módulo no encontrado")
    return module

@router.get("/{module_id}/projects", response_model=List[Project])
def get_module_projects(module_id: int, db: Session = Depends(get_db)):
    projects = db.query(ProjectModel).filter(
        ProjectModel.module_id == module_id
    ).order_by(ProjectModel.order).all()
    return projects

@router.post("/", response_model=Module)
def create_module(module: ModuleCreate, db: Session = Depends(get_db)):
    db_module = ModuleModel(**module.dict())
    db.add(db_module)
    db.commit()
    db.refresh(db_module)
    return db_module
