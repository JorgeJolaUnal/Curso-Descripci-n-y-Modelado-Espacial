# Usa una imagen base de Python
FROM python:3.11-slim

# Instala R y las dependencias necesarias
RUN apt-get update && \
    apt-get install -y \
    r-base \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación escuchará
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000"]
