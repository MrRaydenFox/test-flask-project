# Utilizar una imagen base de Python
FROM python:3.13-slim

# Evitar que Python genere archivos .pyc y establecer salida sin buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar el resto del proyecto
COPY . /app

# Exponer el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "run.py"]
