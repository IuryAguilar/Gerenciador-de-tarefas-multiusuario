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
        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    '''
                    UPDATE tarefas 
                    SET titulo = %s, descricao = %s, status = %s, prioridade = %s, prazo = %s
                    WHERE id = %s
                    AND usuario_id = %s
                    ''',
                    (titulo, descricao, status, prioridade, prazo, tarefa_id, usuario_id)
                )

            conexao.commit()

            return cursor.rowcount

    def identificar_tarefa_por_id(self, tarefa_id, usuario_id):
        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    '''
                    SELECT id
                    FROM tarefas
                    WHERE id = %s AND usuario_id = %s
                    ''',
                    (tarefa_id, usuario_id)
                )

                tarefa_encontrada = cursor.fetchone()

            return tarefa_encontrada

    def excluir_tarefa(self, tarefa_id, usuario_id):
        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    '''
                    DELETE FROM tarefas
                    WHERE id = %s AND usuario_id = %s
                    ''',
                    (tarefa_id, usuario_id)
                )

            conexao.commit()

            return cursor.rowcount