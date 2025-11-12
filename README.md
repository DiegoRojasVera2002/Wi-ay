# Wiñay - Aprende Haciendo 🌱

Plataforma de especialización basada en proyectos reales propuestos por empresas peruanas.

## 🚀 Características

- **Proyectos Reales**: Resuelve desafíos propuestos por startups y empresas tech
- **Certificados Avalados**: Recibe certificados validados por las empresas
- **Aprende Haciendo**: Guías paso a paso con validación automática de código
- **100% Gratuito**: Sin costo para estudiantes universitarios

## 📋 Requisitos

- Python 3.8+
- Node.js 18+
- npm o yarn

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
cd wiñay
```

### 2. Configurar Backend (FastAPI)

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Copiar archivo de configuración
cp .env.example .env
```

### 3. Configurar Frontend (SvelteKit)

```bash
# Instalar dependencias
npm install
```

### 4. Inicializar Base de Datos

```bash
# Llenar con datos de ejemplo
python seed_data.py
```

## ▶️ Ejecutar la Aplicación

### Opción 1: Ejecutar Backend y Frontend por separado

**Terminal 1 - Backend:**
```bash
source venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
npm run dev
```

### Opción 2: Script de inicio rápido

```bash
# Crear script de inicio
chmod +x start.sh
./start.sh
```

## 🌐 Acceder a la Aplicación

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **Documentación API**: http://localhost:8000/docs

## 👤 Usuario de Prueba

```
Email: estudiante@test.com
Password: password123
```

## 📁 Estructura del Proyecto

```
wiñay/
├── app/                    # Backend (FastAPI)
│   ├── main.py            # Aplicación principal
│   ├── database.py        # Configuración de BD
│   ├── models.py          # Modelos SQLAlchemy
│   ├── schemas.py         # Schemas Pydantic
│   └── routes/            # Endpoints de API
│       ├── auth.py
│       ├── modules.py
│       ├── projects.py
│       └── submissions.py
├── src/                   # Frontend (SvelteKit)
│   ├── routes/           # Páginas
│   │   ├── +page.svelte  # Home
│   │   ├── +layout.svelte # Layout global
│   │   ├── login/
│   │   ├── register/
│   │   ├── modules/
│   │   └── dashboard/
│   ├── lib/              # Utilidades
│   │   └── api.js        # Cliente API
│   └── app.css           # Estilos globales
├── requirements.txt       # Dependencias Python
├── package.json          # Dependencias Node.js
└── seed_data.py          # Script de datos iniciales
```

## 📊 Módulos Disponibles

### 1. Data Science para Fintech
- Segmentación de Clientes (PrestaTech)
- Detección de Fraude (PagoSeguro)
- Optimización de Credit Scoring (InnovaBank)

### 2. IoT y Automatización Industrial
- Script de Ingesta de Sensores (AgroData)
- Dashboard de Monitoreo (LogiTrack)
- Sistema de Alerta Automatizada (AgroData)

### 3. Desarrollo Web para Mercado
- Landing Page Profesional (Hashi)
- Plataforma Web con Base de Datos (Ya Vendió)
- E-commerce Completo (Artificio)

## 🔧 Tecnologías

**Backend:**
- FastAPI
- SQLAlchemy
- SQLite
- Python 3.8+

**Frontend:**
- SvelteKit
- Vite
- Axios

## 🎯 Próximas Características

- [ ] Sistema de certificados en PDF
- [ ] Chatbot asistente con IA
- [ ] Módulo de Hackathons
- [ ] Playground con retos de IA
- [ ] Dashboard para empresas

## 📝 Licencia

Este proyecto fue desarrollado para el Fintech Challenge Hackathon.

## 👥 Equipo

Desarrollado con ❤️ por el equipo Wiñay

---

**Wiñay** - Crecer y Desarrollar 🌱
