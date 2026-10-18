from app.controller.tarefa_controller import TarefaController
from app.services.tarefa_service import TarefaService
from app.model.tarefas_model import TarefaModel
from fastapi import Depends

def obter_tarefa_model():
    tarefa_model = TarefaModel()

    return tarefa_model

def obter_tarefa_service(
        tarefa_model: TarefaModel = Depends(obter_tarefa_model)
):
    tarefa_sevice = TarefaService(
        tarefa_model
    )

    return tarefa_sevice

def obter_tarefa_controller(
        tarefa_service: TarefaService = Depends(obter_tarefa_service)
):
    tarefa_controller = TarefaController(
        tarefa_service
    )

    return tarefa_controller