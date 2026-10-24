const createTaskElements = {
    criarTarefa_form: document.getElementById('criarTarefaForm'),
    titulo_input: document.getElementById('tituloI'),
    descricao_input: document.getElementById('descricaoTxtArea'),
    prioridade_select: document.getElementById('prioridadeSlct'),
    status_select: document.getElementById('statusSlct'),
    prazo_input: document.getElementById('prazoI'),
    error_msg: document.getElementById('errorCT'),
    criarTarefa_button: document.getElementById('criarTarefaBtn')
};

const listTaskElements = {
    listaTarefas: document.getElementById('tarefasListadas'),
    error_msg: document.getElementById('errorLT')
};

const editTaskElements = {
    editarTarefa_container: document.querySelector('.editarTarefa-container'),
    editarTarefa_form: document.getElementById('editarTarefaForm'),
    id_input: document.getElementById('tarefaId-edit'),
    titulo_input: document.getElementById('tituloI-edit'),
    descricao_input: document.getElementById('descricaoTxtArea-edit'),
    prioridade_select: document.getElementById('prioridadeSlct-edit'),
    status_select: document.getElementById('statusSlct-edit'),
    prazo_input: document.getElementById('prazoI-edit'),
    error_msg: document.getElementById('errorET-edit'),
    salvarAlteracao_button: document.getElementById('salvarAlteracaoBtn-edit'),
    cancelarAlteracao_button: document.getElementById('cancelarAlteracaoBtn-edit')
};

const token = localStorage.getItem("token");

createTaskElements.criarTarefa_form.addEventListener("submit", async (event) => {
    event.preventDefault();

    createTaskElements.error_msg.textContent = "";

    const titulo = createTaskElements.titulo_input.value.trim();
    const descricao = createTaskElements.descricao_input.value || null;
    const prioridade = createTaskElements.prioridade_select.value;
    const status = createTaskElements.status_select.value;
    const prazo = createTaskElements.prazo_input.value || null;

    if (titulo === ""){
        createTaskElements.error_msg.textContent = "Campo de Título obrigatório.";
        return;
    };

    const tarefa = {
        titulo,
        descricao,
        prioridade,
        status,
        prazo
    };

    if (!token){
        createTaskElements.error_msg.textContent = "Faça login antes de continuar";
        return;
    };

    try{
        const resposta = await fetch("http://127.0.0.1:8000/criar_tarefa", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify(tarefa)
        });

        const dados = await resposta.json();

        if (!resposta.ok){
            createTaskElements.error_msg.textContent = "Erro ao criar a tarefa.";
        } else {
            createTaskElements.error_msg.textContent = "Tarefa criada com sucesso.";
            createTaskElements.criarTarefa_form.reset();
            await listar_tarefas();
            return;
        };
    } catch (erro) {
        console.error("Ops, algo deu errado:", erro.message);
    };
});

async function listar_tarefas(){
    try{
        const resposta = await fetch("http://127.0.0.1:8000/listar_tarefas", {
            method: "GET",
            headers: {
                'Content-Type': 'application/json',
                "Authorization": `Bearer ${token}`
            }
        });

        const dados = await resposta.json();

        const statusLabels = {
            pendente: "Pendente",
            em_andamento: "Em andamento",
            concluida: "Concluída"
        }

        if (!resposta.ok){
            listTaskElements.error_msg.textContent = "Erro ao listar as tarefas.";
        } else {
            listTaskElements.listaTarefas.textContent = "";
            for (let dado of dados) {
                const item = document.createElement("li");

                const infoEscondida = document.createElement("div");
                infoEscondida.classList.add("infoEscondida")

                let titulo = document.createElement("h2");
                titulo.textContent = dado[1].charAt(0).toUpperCase() + dado[1].slice(1);
                item.appendChild(titulo);

                let descricao = document.createElement("p");
                if (!dado[2]) {
                    descricao.textContent = "Sem descrição";
                } else {
                    descricao.textContent = dado[2].charAt(0).toUpperCase() + dado[2].slice(1);
                };
                infoEscondida.appendChild(descricao);
                item.appendChild(infoEscondida);

                let status = document.createElement("p");
                status.textContent = statusLabels[dado[3]] || "Status desconhecido";
                item.appendChild(status);

                let prioridade = document.createElement("p");
                prioridade.textContent = dado[4].charAt(0).toUpperCase() + dado[4].slice(1);
                item.appendChild(prioridade);

                let prazo = document.createElement("p");
                if (!dado[5]) {
                    prazo.textContent = "Sem prazo";
                } else {
                    const data = dado[5].split("-")
                    prazo.textContent = data[2] + "/" + data[1] + "/" + data[0]
                };
                item.appendChild(prazo);

                const deletarTarefaBtn = document.createElement("button");
                deletarTarefaBtn.textContent = "Excluir";
                deletarTarefaBtn.dataset.tarefaId = dado[0];
                item.appendChild(deletarTarefaBtn);

                deletarTarefaBtn.addEventListener("click", async () => {
                    const tarefaId = deletarTarefaBtn.dataset.tarefaId;
                    
                    try {
                        const resposta = await fetch(`http://127.0.0.1:8000/excluir_tarefa/${tarefaId}`, {
                            method: "DELETE",
                            headers: {
                                'Content-Type': 'application/json',
                                "Authorization": `Bearer ${token}`
                            }
                        })

                        if (!resposta.ok) {
                            listTaskElements.error_msg.textContent = "Erro ao excluir a tarefa.";
                        } else {
                            listar_tarefas();
                        }
                    } catch (erro) {
                        console.error("Ops, algo deu errado:", erro.message);
                    }
                });

                const editarTarefaBtn = document.createElement("button");
                editarTarefaBtn.textContent = "Editar";
                editarTarefaBtn.dataset.tarefaId = dado[0];
                item.appendChild(editarTarefaBtn);

                editarTarefaBtn.addEventListener("click", async () => {
                    const tarefaId = editarTarefaBtn.dataset.tarefaId;

                    editTaskElements.editarTarefa_container.style.display = "flex";

                    editTaskElements.id_input.value = tarefaId;
                    editTaskElements.titulo_input.value = dado[1];
                    editTaskElements.descricao_input.value = dado[2] || "";
                    editTaskElements.status_select.value = dado[3];
                    editTaskElements.prioridade_select.value = dado[4];
                    editTaskElements.prazo_input.value = dado[5] || "";
                });

                listTaskElements.listaTarefas.appendChild(item);
            };
            return;
        }
    } catch (erro) {
        console.error("Ops, algo deu errado:", erro.message);
    };
};
listar_tarefas();

editTaskElements.cancelarAlteracao_button.addEventListener("click", () => {
    editTaskElements.editarTarefa_container.style.display = "none";

    editTaskElements.editarTarefa_form.reset();

    editTaskElements.error_msg.textContent = "";
});

editTaskElements.editarTarefa_form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const tarefaId = editTaskElements.id_input.value;

    const titulo = editTaskElements.titulo_input.value.trim();
    const descricao = editTaskElements.descricao_input.value || null;
    const prioridade = editTaskElements.prioridade_select.value;
    const status = editTaskElements.status_select.value;
    const prazo = editTaskElements.prazo_input.value || null;

    const tarefaEditada = {
        titulo,
        descricao,
        prioridade,
        status,
        prazo
    };

    try{
        const resposta = await fetch(`http://127.0.0.1:8000/atualizar_tarefa/${tarefaId}`, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json',
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify(tarefaEditada)
        });

        if (!resposta.ok){
            editTaskElements.error_msg.textContent = "Erro ao alterar tarefa.";
        } else {
            editTaskElements.editarTarefa_container.style.display = "none"
            editTaskElements.editarTarefa_form.reset();
            await listar_tarefas();
            return;
        };
    } catch(erro) {
        console.error("Ops, algo deu errado:", erro.message);
    }
});