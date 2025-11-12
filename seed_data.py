"""
Script para llenar la base de datos con datos de ejemplo
"""
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import Module, Project, Step, User, DifficultyLevel
import json
import bcrypt

def seed_database():
    # Create tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # Check if data already exists
        if db.query(Module).first():
            print("Database already has data. Skipping seed.")
            return

        print("Seeding database...")

        # Create example user
        password = "password123"
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User(
            email="estudiante@test.com",
            hashed_password=hashed,
            full_name="Juan Pérez",
            role="student",
            university="Universidad Nacional Mayor de San Marcos"
        )
        db.add(user)

        # Module 1: Data Science para Fintech
        module1 = Module(
            title="Data Science para Fintech",
            description="Aprende a construir soluciones de IA para el sector financiero",
            category="Data Science",
            icon="📊"
        )
        db.add(module1)
        db.flush()

        # Projects for Module 1
        project1_1 = Project(
            module_id=module1.id,
            title="Segmentación de Clientes",
            description="Analiza un dataset de transacciones para identificar patrones de gasto usando K-Means",
            company_name="PrestaTech",
            difficulty=DifficultyLevel.BEGINNER,
            order=1
        )
        db.add(project1_1)
        db.flush()

        # Steps for Project 1.1
        step1 = Step(
            project_id=project1_1.id,
            title="Limpieza de Datos con Pandas",
            description="Aprende a manejar valores nulos y atípicos en datasets financieros",
            content="""
# Paso 1: Limpieza de Datos

En este paso, aprenderás a limpiar datos de transacciones financieras.

## Recursos
- Video tutorial: Introducción a Pandas
- Documentación: pandas.pydata.org

## Tu Tarea
Crea una función llamada `solution(data)` que:
1. Reciba un diccionario con datos de transacciones
2. Elimine las transacciones con monto negativo
3. Retorne el total de transacciones válidas

Ejemplo:
```python
def solution(data):
    # Tu código aquí
    pass
```
            """,
            test_input=json.dumps([
                {"transactions": [100, 200, -50, 300]},
                {"transactions": [50, 75, -10, 125, 200]}
            ]),
            test_output=json.dumps([3, 4]),
            order=1
        )
        db.add(step1)

        step2 = Step(
            project_id=project1_1.id,
            title="Ingeniería de Atributos",
            description="Crea variables útiles para el modelo de clustering",
            content="""
# Paso 2: Ingeniería de Atributos

Aprende a crear features (características) útiles para análisis de clientes.

## Tu Tarea
Crea una función que calcule el gasto promedio de las transacciones.
            """,
            test_input=json.dumps([
                {"transactions": [100, 200, 300]},
                {"transactions": [50, 150]}
            ]),
            test_output=json.dumps([200, 100]),
            order=2
        )
        db.add(step2)

        # Project 1.2
        project1_2 = Project(
            module_id=module1.id,
            title="Detección de Fraude",
            description="Construye un modelo de IA que detecte transacciones anómalas en tiempo real",
            company_name="PagoSeguro",
            difficulty=DifficultyLevel.INTERMEDIATE,
            order=2
        )
        db.add(project1_2)

        # Module 2: IoT y Automatización
        module2 = Module(
            title="IoT y Automatización Industrial",
            description="Desarrolla soluciones de IoT para agricultura y logística",
            category="IoT",
            icon="🔌"
        )
        db.add(module2)
        db.flush()

        # Project 2.1
        project2_1 = Project(
            module_id=module2.id,
            title="Script de Ingesta de Sensores",
            description="Escribe un script en Python que procese datos de sensores IoT",
            company_name="AgroData",
            difficulty=DifficultyLevel.BEGINNER,
            order=1
        )
        db.add(project2_1)
        db.flush()

        step2_1 = Step(
            project_id=project2_1.id,
            title="Conexión y Filtrado de Datos",
            description="Filtra y limpia lecturas de sensores de humedad",
            content="""
# Conexión a Sensores IoT

Aprende a procesar datos de sensores en tiempo real.

## Tu Tarea
Crea una función que filtre lecturas inválidas (humedad > 100 o < 0).
            """,
            test_input=json.dumps([
                {"readings": [45, 67, 120, 89]},
                {"readings": [-5, 34, 56, 78]}
            ]),
            test_output=json.dumps([3, 3]),
            order=1
        )
        db.add(step2_1)

        # Project 2.2
        project2_2 = Project(
            module_id=module2.id,
            title="Dashboard de Monitoreo",
            description="Crea un dashboard web que muestre datos de temperatura en tiempo real",
            company_name="LogiTrack",
            difficulty=DifficultyLevel.INTERMEDIATE,
            order=2
        )
        db.add(project2_2)

        # Module 3: Desarrollo Web
        module3 = Module(
            title="Desarrollo Web para Mercado",
            description="Construye aplicaciones web modernas para startups peruanas",
            category="Web Development",
            icon="💻"
        )
        db.add(module3)
        db.flush()

        project3_1 = Project(
            module_id=module3.id,
            title="Landing Page Profesional",
            description="Diseña y desarrolla una landing page responsive",
            company_name="Hashi",
            difficulty=DifficultyLevel.BEGINNER,
            order=1
        )
        db.add(project3_1)

        project3_2 = Project(
            module_id=module3.id,
            title="Plataforma Web con Base de Datos",
            description="Desarrolla una aplicación web completa con backend",
            company_name="Ya Vendió",
            difficulty=DifficultyLevel.INTERMEDIATE,
            order=2
        )
        db.add(project3_2)

        project3_3 = Project(
            module_id=module3.id,
            title="E-commerce Completo",
            description="Construye una tienda online con carrito y pagos",
            company_name="Artificio",
            difficulty=DifficultyLevel.ADVANCED,
            order=3
        )
        db.add(project3_3)

        db.commit()
        print("✅ Database seeded successfully!")
        print("\nExample user created:")
        print("  Email: estudiante@test.com")
        print("  Password: password123")

    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
