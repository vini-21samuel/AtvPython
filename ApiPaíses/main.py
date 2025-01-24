from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# Criando a instância da aplicação FastAPI
app = FastAPI()

# Base de dados de exemplo: Lista de países com suas capitais, populações e continentes
banco_de_paises = [
    {"nome_pais": "Senegal", "capital": "Dacar", "populacao": 16700000, "continente": "África"},
    {"nome_pais": "Austrália", "capital": "Camberra", "populacao": 25687041, "continente": "Oceania"},
    {"nome_pais": "Líbano", "capital": "Beirute", "populacao": 6825445, "continente": "Ásia"},
    {"nome_pais": "Mongólia", "capital": "Ulaanbaatar", "populacao": 3300000, "continente": "Ásia"},
]

# 0. Rota principal: Listar todos os países
@app.get("/")
async def listar_todos_paises():
    return banco_de_paises

# 1. Consultar informações de um país (Parâmetro de Caminho)
@app.get("/pais/{nome_pais}")
async def consultar_pais(nome_pais: str):
    for pais in banco_de_paises:
        if pais["nome_pais"].lower() == nome_pais.lower():
            return pais
    return {"erro": "País não encontrado"}

# 2. Filtrar países por continente (Parâmetro de Consulta)
@app.get("/paises/")
async def filtrar_paises_por_continente(continente: Optional[str] = None):
    if continente:
        paises_filtrados = [pais for pais in banco_de_paises if pais["continente"].lower() == continente.lower()]
        return paises_filtrados
    return banco_de_paises

# 3. Adicionar um novo país (Parâmetro de Caminho e Corpo da Requisição)
class Pais(BaseModel):
    capital: str
    populacao: int
    continente: str

@app.post("/pais/{nome_pais}")
async def adicionar_pais(nome_pais: str, pais: Pais):
    # Verificar se o país já existe
    for p in banco_de_paises:
        if p["nome_pais"].lower() == nome_pais.lower():
            return {"erro": "O país já existe na base de dados"}
    
    # Adicionando o novo país
    banco_de_paises.append({
        "nome_pais": nome_pais,
        "capital": pais.capital,
        "populacao": pais.populacao,
        "continente": pais.continente
    })
    
    return {"mensagem": "País adicionado com sucesso!", "nome_pais": nome_pais}
