class Anexo: #Vitor

    def __init__(self, nome: str, caminho:str):
        self.__id = id
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def caminho(self):
        return self.__caminho

    @caminho.setter
    def caminho(self, caminho: str):
        self.__caminho = caminho