class TarefaService:
    def __init__(self, tarefa_model):
        self.tarefa_model = tarefa_model

    def listar_tarefas(self, usuario_id):
        resultado_listagem = self.tarefa_model.listar_tarefas(usuario_id)

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
        self.tarefa_model.criar_tarefa(
            titulo,
            descricao,
            status,
            prioridade,
            prazo,
            usuario_id
        )

        return True