from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_usuario, rotas_empresa, rotas_passagem

app = FastAPI()

# CORS
origins = ['http://localhost:5500']

app.add_middleware(CORSMiddleware, 
                    allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],)

# Rotas do  Usuário
app.include_router(rotas_usuario.router)

# Rotas  da Empresa
app.include_router(rotas_empresa.router)

# Rotas  da Passagem
app.include_router(rotas_passagem.router)