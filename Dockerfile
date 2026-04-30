# 1. Imagen ligera de Python
FROM python:3.11-slim

# 2. Carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Instalación de Flask
RUN pip install flask

# 4. Copia de archivos al contenedor
COPY app.py .
COPY datos.json .

# 5. Se especifica puerto 5000 donde estará abierto
EXPOSE 5000

# 6. Comando para arrancar la app al encender el contenedor
CMD ["python", "app.py"]
