from datetime import datetime
from Usuarios import Pac, Tecnico
from Classes_suporte import Anexo, Avaliacao, Categoria,\
                            Comentario, Prioridade, Status


class Chamado: #Gabriel

    def __init__(self, id_chamado:int, titulo:str, descricao:str, #1
                        status:Status, prioridade:Prioridade, categoria:Categoria, sala:str, #2
                        tecnico_responsavel:Tecnico, solicitante:Pac): #3

    #área de informação do chamado - 1
        self.__id_chamado = id_chamado
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_abertura = datetime.now()
        self.__data_fechamento = None
        self.__comentario = None
        self.__anexos = None

    #área de controle do chamado - 2
        self.__status = status
        self.__prioridade = prioridade
        self.__categoria = categoria
        self.__sala = sala

    #envolvidos no chamado - 3
        self.__responsavel = tecnico_responsavel
        self.__solicitante = solicitante
