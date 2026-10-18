from fastapi import APIRouter, Depends
from app.controller.tarefa_controller import TarefaController
from app.dependencies.tarefa_dependencies import obter_tarefa_controller
from app.dependencies.auth_dependencies import verificar_autentificacao
from app.schemas.tarefa_schema import TarefaCriacao

router = APIRouter()

@router.get("/listar_tarefas")
def listar_tarefas(
    usuario: dict = Depends(verificar_autentificacao),
    tarefa_controller: TarefaController = Depends(obter_tarefa_controller)
):
    usuario_id = usuario["sub"]

    tarefas_listadas = tarefa_controller.listar_tarefas(usuario_id)

    return tarefas_listadas

@router.post("/criar_tarefa")
def criar_tarefa(
    tarefa: TarefaCriacao,
    usuario: dict = Depends(verificar_autentificacao),
    tarefa_controller: TarefaController = Depends(obter_tarefa_controller)
):
    usuario_id = usuario["sub"]
    
    resultado_criacao = tarefa_controller.criar_tarefa(
        tarefa.titulo,
        tarefa.descricao,
        tarefa.status,
        tarefa.prioridade,
        tarefa.prazo,
        usuario_id
    )

    return resultado_criacao