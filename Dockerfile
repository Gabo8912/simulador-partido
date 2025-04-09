# Usa una imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos al contenedor
COPY . /app

# Comando por defecto para ejecutar tu programa
CMD ["python", "simulador.py"]
