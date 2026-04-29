# 2. Crie o ambiente virtual (garante que as bibliotecas não conflitem com outras)
# as libs só ficam presentes nesse projeto e não globalmente (esse comando só precisa ser rodado uma vez para criar o ambiente virtual)
python -m venv venv

# 3. Ative o ambiente virtual
# No Windows:
.\venv\Scripts\activate

# 4. Instale o FastAPI e o servidor Uvicorn (o motor que roda a API)
pip install fastapi "uvicorn[standard]"

# Lista de dependências
(gere com: pip freeze > requirements.txt)

# para rodar o projeto
uvicorn app.main:app --reload