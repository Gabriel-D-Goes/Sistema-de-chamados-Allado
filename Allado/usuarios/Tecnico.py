from Usuario import Usuario

class Tecnico(Usuario): #Gabriel

    def __init__(self, nome:str, cpf:str, senha:str,
                                avaliacao, cargo:str):
        
        super().__init__(nome, cpf, senha)
        self.__avaliacao = avaliacao
        self.__cargo = cargo