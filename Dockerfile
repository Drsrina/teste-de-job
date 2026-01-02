# Usa uma imagem Python leve
FROM python:3.9-slim

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia o script para dentro do container
COPY main.py .

# Comando para rodar o script quando o container iniciar
CMD ["python", "main.py"]