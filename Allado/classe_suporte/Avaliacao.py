class Avaliacao: #Vitor

    def __init__(self, id_avaliador:int, id_chamado:int, id_tecnico:int, nota:int):
        self.__id_avaliador = id_avaliador
        self.__id_chamado = id_chamado
        self.__id_tecnico = id_tecnico
        self.__nota = nota

    @property
    def id_avaliador(self):
        return self.__id_avaliador

    @property
    def id_chamado(self):
        return self.__id_chamado

    @property
    def id_tecnico(self):
        return self.__id_tecnico

    @property
    def nota(self):
        return self.__nota

    @id_avaliador.setter
    def id_avaliador(self, id_avaliador:int):
        self.__id_avaliador = id_avaliador

    @id_chamado.setter
    def id_chamado(self, id_chamado:int):
        self.__id_chamado = id_chamado

    @id_tecnico.setter
    def id_tecnico(self, id_tecnico:int):
        self.__id_tecnico = id_tecnico

    @nota.setter
    def nota(self, nota:int):
        self.__nota = nota