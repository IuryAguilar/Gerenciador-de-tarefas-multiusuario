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

    def atualizar_tarefa(
        self,
        tarefa_id,
        titulo,
        descricao,
        status,
        prioridade,
        prazo,
        usuario_id
    ):
        resultado_atualizacao = self.tarefa_service.atualizar_tarefa(
            tarefa_id,
            titulo,
            descricao,
            status,
            prioridade,
            prazo,
            usuario_id
        )

        if resultado_atualizacao > 0:
            return {
                "sucesso": True,
                "mensagem": "Tarefa atualizada com sucesso."
            }
        else:
            return {
                "sucesso": True,
                "mensagem": "Nenhuma alteração foi necessária."
            }

    def excluir_tarefa(self, tarefa_id, usuario_id):
        resultado_exclusao = self.tarefa_service.excluir_tarefa(
            tarefa_id,
            usuario_id
        )

        if resultado_exclusao > 0:
            return {
                "sucesso": True,
                "mensagem": "Tarefa excluída com sucesso."
            }
        else:
            return {
                "sucesso": False,
                "mensagem": "Nenhuma tarefa excluída."
            }



