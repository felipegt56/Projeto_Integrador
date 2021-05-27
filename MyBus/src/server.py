from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_usuario, rotas_empresa

app = FastAPI()

# CORS
origins = ['http://localhost:3000', 
            'http://myapp.vercel.com']

app.add_middleware(CORSMiddleware, 
                    allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],)


app.include_router(rotas_usuario.router)
app.include_router(rotas_empresa.router)

#app.include_router(rotas_pedidos.router)