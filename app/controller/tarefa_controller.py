class TarefaController:
    def __init__(self, tarefa_service):
        self.tarefa_service = tarefa_service

    def listar_tarefas(self, usuario_id):
        resultado_listagem = self.tarefa_service.listar_tarefas(usuario_id)    

        return resultado_listagem

    def criar_tarefa(
            self,
            titulo,
            descricao,
            status,
            prioridade,
            prazo,
            usuario_id
    ):
        resultado_criacao = self.tarefa_service.criar_tarefa(
            titulo,
            descricao,
            status,
            prioridade,
            prazo,
            usuario_id
        )

        if resultado_criacao:
            return {
                "sucesso": True,
                "mensagem": "Tarefa criada com sucesso."
            }

