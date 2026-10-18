from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware 
from app.exceptions import (
    UsuarioNaoEncontradoException,
    UsuarioJaEncontradoException,
    EmailOuSenhaInvalidoException,
    TarefaNaoEncontradaException
    )
from app.routers.auth_router import router as auth_router
from app.routers.usuario_router import router as usuario_router
from app.routers.tarefa_router import router as tarefa_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(usuario_router)
app.include_router(tarefa_router)

@app.exception_handler(UsuarioJaEncontradoException)
def usuario_ja_encontrado_handler(request, exc):
    return JSONResponse(
        status_code = 400,
        content ={
            "detail": str(exc)
        }
    )


@app.exception_handler(UsuarioNaoEncontradoException)
def usuario_nao_encontrado_handler(request, exc):
    return JSONResponse(
        status_code = 404,
        content ={
            "detail": str(exc)
        }
    )

@app.exception_handler(EmailOuSenhaInvalidoException)
def email_ou_senha_invalido_handler(request, exc):
    return JSONResponse(
        status_code = 401,
        content ={
            "detail": str(exc)
        }
    )

@app.exception_handler(TarefaNaoEncontradaException)
def tarefa_nao_encontrada_handler(request, exc):
    return JSONResponse(
        status_code = 404,
        content = {
            "detail": str(exc)
        }
    )