from abc import ABC, abstractmethod

class SuporteBase(ABC): #Vitor

    def __init__(self, id:int, nome:str):

        self.__id = id
        self.__nome = nome

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @id.setter
    def id(self, id:int):
        self.__id = id

    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome