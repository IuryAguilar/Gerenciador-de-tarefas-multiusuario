from app.database.database import conectar_banco

class TarefaModel:
    def criar_tarefa(
            self,
            titulo,
            descricao,
            status,
            prioridade,
            prazo,
            usuario_id
    ):
        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    '''  
                    INSERT INTO tarefas (titulo, descricao, status, prioridade, prazo,
                    usuario_id)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ''',
                    (titulo, descricao, status, prioridade, prazo, usuario_id)
                )

            conexao.commit()

    def listar_tarefas(self, usuario_id):
        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM tarefas WHERE usuario_id = %s",
                    (usuario_id,)
                )

                resultado_tarefas = cursor.fetchall()

                return resultado_tarefas