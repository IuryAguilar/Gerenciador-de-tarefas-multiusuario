from pydantic import BaseModel
from datetime import date
from enum import Enum

class StatusTarefa(str, Enum):
    PENDENTE = "pendente"
    EM_ANDAMENTO = "em_andamento"
    CONCLUIDA = "concluida"

class PrioridadeTarefa(str, Enum):
    BAIXA = "baixa"
    MEDIA = "media"
    ALTA = "alta"

class TarefaCriacao(BaseModel):
    titulo: str
    descricao: str | None = None
    status: StatusTarefa = "pendente"
    prioridade: PrioridadeTarefa = "media"
    prazo: date | None = None

