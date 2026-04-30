# Proyecto Integrador: Chatbot con Flask y Docker

Este proyecto es una API de chatbot que responde preguntas desde un archivo JSON, diseñada para demostrar el uso de Docker y Docker Compose.

## Características
- **Flask API**: Microservicio en Python.
- **Docker**: Contenerización con imagen ligera de Python.
- **Docker Compose**: Orquestación del servicio.
- **Persistencia**: Uso de volúmenes para el archivo de datos `datos.json`.

## Cómo ejecutar
1. Tener instalado Docker y Docker Compose.
2. Ejecutar: `sudo docker compose up -d`
3. Probar en: `http://localhost:5000/chat?pregunta=volumen`
