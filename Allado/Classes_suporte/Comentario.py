from datetime import date


class Comentario: #Vitor

    def __init__(self, data:date, id_chamado:int, mensagem:str):
        self.__data = data
        self.__id_chamado = id_chamado
        self.__mensagem = mensagem

    @property
    def data(self):
        return self.__data

    @property
    def id_chamado(self):
        return self.__id_chamado

    @property
    def mensagem(self):
        return self.__mensagem

    @id_chamado.setter
    def id_chamado(self, id_chamado:int):
        self.__id_chamado = id_chamado

    @mensagem.setter
    def mensagem(self, mensagem:str):
        self.__mensagem = mensagem