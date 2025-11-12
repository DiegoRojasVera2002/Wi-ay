from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from .database import engine, Base
from .routes import auth, modules, projects, submissions

# Load environment variables
load_dotenv()

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Wiñay - Aprende Haciendo",
    description="Plataforma de especialización basada en proyectos reales",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(modules.router, prefix="/api/modules", tags=["modules"])
app.include_router(projects.router, prefix="/api/projects", tags=["projects"])
app.include_router(submissions.router, prefix="/api/submissions", tags=["submissions"])

@app.get("/")
def root():
    return {
        "message": "Wiñay API - Aprende Haciendo",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
