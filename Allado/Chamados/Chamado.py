from datetime import datetime


class Chamado: #Gabriel

    def __init__(self, id_chamado:int, titulo, descricao, #1
                        status, prioridade, categoria, sala, #2
                        tecnico_responsavel, solicitante): #3

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
