from app.exceptions import TarefaNaoEncontradaException

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
        self.identificar_tarefa_por_id(tarefa_id, usuario_id)
        
        resultado_atualizacao = self.tarefa_model.atualizar_tarefa(
            tarefa_id,
            titulo,
            descricao,
            status,
            prioridade,
            prazo,
            usuario_id
        )

        return resultado_atualizacao

    def identificar_tarefa_por_id(self, tarefa_id, usuario_id):
        tarefa_identificada = self.tarefa_model.identificar_tarefa_por_id(
            tarefa_id,
            usuario_id
        )

        if tarefa_identificada is None:
            raise TarefaNaoEncontradaException(
                "Tarefa não encontrada."
            )

        return tarefa_identificada

    def excluir_tarefa(self, tarefa_id, usuario_id):
        self.identificar_tarefa_por_id(tarefa_id, usuario_id)

        resultado_exclusao = self.tarefa_model.excluir_tarefa(
            tarefa_id,
            usuario_id
        )

        return resultado_exclusao