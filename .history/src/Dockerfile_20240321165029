FROM python:3.12-slim-bullseye

# Instalar dependencias adicionales
RUN apt-get update && apt-get install -y python3-dev python3-dev gcc

# Actualizar numpy y scikit-learn
RUN pip install --upgrade numpy scikit-learn

# Copiar el archivo requirements.txt
COPY requirements.txt .

# Instalar las dependencias del proyecto
RUN pip install -r requirements.txt

# Copiar la aplicación
COPY ./App /app

# Establecer directorio de trabajo
WORKDIR /app

# Exponer el puerto 5000
EXPOSE 5000

# Comando por defecto para ejecutar la aplicación
CMD ["python3", "app.py"]