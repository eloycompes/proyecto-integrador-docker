# 🤖🐳 Chatbot Dockerizado - Proyecto Integrador

![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![Python](https://img.shields.io/badge/Python-3.11-yellow?logo=python)
![Flask](https://img.shields.io/badge/Flask-API-black?logo=flask)
![Status](https://img.shields.io/badge/Estado-Funcional-brightgreen)

---

# 📌 Descripción

Este proyecto consiste en un **chatbot técnico sobre Docker**, desarrollado con **Flask** y ejecutado dentro de contenedores con **Docker y Docker Compose**.

El chatbot funciona como una API REST que:

✅ Lee información desde un archivo `datos.json`  
✅ Procesa preguntas técnicas  
✅ Busca coincidencias mediante **intersección de palabras clave** usando estructuras `set()` de Python  
✅ Devuelve respuestas relacionadas con comandos y conceptos de Docker  

---

# 🛠 Tecnologías utilizadas

| Tecnología | Uso |
|------------|-----|
| 🐍 Python 3.11-slim | Backend |
| ⚡ Flask | API REST |
| 🐳 Docker | Contenerización |
| 📦 Docker Compose | Orquestación |
| 📄 JSON | Base de conocimiento |

---

# 📂 Estructura del proyecto

```bash
proyecto-integrador-docker/
│
├── app.py
├── datos.json
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# 🚀 Instalación paso a paso

## 1️⃣ Clonar repositorio

```bash
git clone https://github.com/eloycompes/proyecto-integrador-docker.git
```

Entrar al proyecto:

```bash
cd proyecto-integrador-docker
```

---

## 2️⃣ Construir la imagen Docker

```bash
sudo docker build -t chatbot .
```

Este comando:

- 📦 Lee el `Dockerfile`
- 🏗 Construye la imagen
- 🏷 La etiqueta como `chatbot`

---

## 3️⃣ Ejecutar con Docker Compose

```bash
sudo docker compose up -d
```

Este comando:

- 🚀 Crea y levanta el contenedor
- 🌐 Expone el servicio en el puerto `5000`
- 📂 Monta un **volumen persistente** para `datos.json`

### ¿Por qué usamos volumen?

El volumen permite que el archivo `datos.json`:

✅ Persista aunque el contenedor se reinicie  
✅ Pueda editarse directamente desde el host  
✅ No requiera reconstruir la imagen para actualizar respuestas  

Ejemplo conceptual:

```yaml
volumes:
  - ./datos.json:/app/datos.json
```

---

## 4️⃣ Probar la API

Abrir en navegador:

```bash
http://localhost:5000/chat?pregunta=docker%20run
```

O con curl:

```bash
curl "http://localhost:5000/chat?pregunta=docker%20run"
```

---

# 🐳 Explicación de Docker

## 📦 Dockerfile

El archivo `Dockerfile` define cómo construir la imagen del proyecto.

Incluye:

- Imagen base `python:3.11-slim`
- Instalación de dependencias
- Copia del código fuente
- Configuración de ejecución

### Flujo:

```bash
Código fuente → Dockerfile → Imagen Docker → Contenedor
```

---

# 🐳📦 Explicación de Docker Compose

El archivo `docker-compose.yml` permite levantar todo el proyecto con un solo comando.

### Incluye:

✅ Construcción automática  
✅ Asignación de puertos  
✅ Montaje de volúmenes  
✅ Gestión simplificada del contenedor  
✅ Persistencia de `datos.json`

### Configuración del volumen

```yaml
services:
  chatbot:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./datos.json:/app/datos.json
```

### Ventajas del volumen

| Beneficio | Explicación |
|-----------|-------------|
| Persistencia | Los datos no se pierden al reiniciar |
| Flexibilidad | Se puede editar desde el host |
| Desarrollo rápido | No requiere rebuild |

---

# 🧠 Funcionamiento interno del chatbot

El chatbot utiliza una lógica de coincidencia basada en conjuntos (`set`).

### Proceso:

1. Usuario envía una pregunta
2. Se separan las palabras clave
3. Se comparan con el contenido de `datos.json`
4. Se calcula la intersección
5. Se devuelve la mejor coincidencia

### Ejemplo conceptual

```python
pregunta_usuario & palabras_clave_json
```

### Ejemplo de estructura del archivo

```json
[
  {
    "pregunta": ["docker", "run"],
    "respuesta": "docker run permite ejecutar contenedores."
  }
]
```

---

# 🛠 Solución de problemas

| Problema ⚠️ | Causa probable | Solución ✅ |
|-------------|----------------|-------------|
| Puerto 5000 ocupado | Otro servicio está usando el puerto | Cambiar puerto en `docker-compose.yml` |
| Permiso denegado | Docker requiere privilegios | Ejecutar con `sudo` |
| Contenedor no inicia | Error en configuración | Revisar logs con `docker logs` |
| No encuentra datos.json | Volumen mal configurado | Verificar rutas del compose |

---

## Ver logs del contenedor

```bash
sudo docker ps
```

Luego:

```bash
sudo docker logs <container_id>
```

---

# 🌿 Organización de ramas

Este proyecto sigue una estrategia simple de ramas:

| Rama | Propósito |
|------|------------|
| `main` | Versión estable y funcional |
| `desarrollo` | Nuevas mejoras y pruebas |

---

## Flujo de trabajo

### Trabajar en desarrollo

```bash
git checkout desarrollo
```

### Subir cambios

```bash
git add .
git commit -m "Nueva funcionalidad"
git push origin desarrollo
```

### Integrar a producción

```bash
git checkout main
git merge desarrollo
git push origin main
```

---


# ⭐ Objetivo académico

Este proyecto demuestra conocimientos en:

✅ Dockerización de aplicaciones  
✅ APIs REST con Flask  
✅ Persistencia con volúmenes  
✅ Orquestación con Docker Compose  
✅ Gestión de ramas con Git  

---
