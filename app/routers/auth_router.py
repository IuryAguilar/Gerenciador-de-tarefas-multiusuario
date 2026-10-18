from fastapi import APIRouter, Depends
from app.controller.auth_controller import AuthController
from app.schemas.usuario_schemas import Cadastro, Login
from app.dependencies.usuario_dependencies import obter_auth_controller

router = APIRouter()

@router.post("/cadastro")
def cadastro(
    usuario: Cadastro,
    auth_controller: AuthController = Depends(obter_auth_controller)
):

    resposta_cadastro = auth_controller.cadastro_usuario(
        usuario.nome,
        usuario.email,
        usuario.senha
    )

    return resposta_cadastro

@router.post("/login")
def login(
    usuario: Login,
    auth_controller: AuthController = Depends(obter_auth_controller)
):

    resposta_login = auth_controller.login_usuario(
        usuario.email,
        usuario.senha
    )

    return resposta_login