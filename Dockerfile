
# Utiliza Python 3.13 em uma imagem Linux enxuta
FROM python:3.13-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia a lista de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos do projeto
COPY . .

# Documenta a porta utilizada pela aplicação
EXPOSE 5000

# Inicia a aplicação com Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
