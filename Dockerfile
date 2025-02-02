# Usa una imagen base de Python
FROM python:3.11-slim

# Instalar R y dependencias necesarias
RUN apt-get update && \
    apt-get install -y r-base && \
    rm -rf /var/lib/apt/lists/*

# Verificar la ubicación de Rscript
RUN echo "Verificando la ubicación de Rscript:" && \
    which Rscript

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . /app

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que la aplicación escuchará
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000"]
