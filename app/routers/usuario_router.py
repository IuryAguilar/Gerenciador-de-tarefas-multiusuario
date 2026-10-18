from fastapi import APIRouter, Depends
from app.controller.auth_controller import AuthController
from app.schemas.usuario_schemas import Perfil
from app.dependencies.usuario_dependencies import obter_auth_controller
from app.dependencies.auth_dependencies import verificar_autentificacao

router = APIRouter()

@router.get("/perfil", response_model = Perfil)
def perfil(
    usuario: dict = Depends(verificar_autentificacao),
    auth_controller: AuthController = Depends(obter_auth_controller)
):
    usuario_id = usuario["sub"]

    perfil_usuario = auth_controller.obter_perfil(usuario_id)

    return perfil_usuario