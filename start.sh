#!/bin/bash

echo "🌱 Iniciando Wiñay..."
echo ""

# Activar entorno virtual y ejecutar backend
echo "📦 Iniciando Backend (FastAPI)..."
source .venv/bin/activate
uvicorn app.main:app --reload --port 8000 &
BACKEND_PID=$!

# Dar tiempo al backend para iniciar
sleep 3

# Ejecutar frontend
echo "🎨 Iniciando Frontend (SvelteKit)..."
npm run dev &
FRONTEND_PID=$!

echo ""
echo "✅ Aplicación iniciada!"
echo ""
echo "Frontend: http://localhost:5173"
echo "Backend: http://localhost:8000"
echo "API Docs: http://localhost:8000/docs"
echo ""
echo "Presiona Ctrl+C para detener"

# Esperar a que se presione Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
