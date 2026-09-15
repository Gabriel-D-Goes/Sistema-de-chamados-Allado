from Usuario import Usuario

class Pac(Usuario): #Gabriel

    def __init__(self, nome:str, cpf:str, senha:str,
                        departamento:str, ramal:int):

        super().__init__(nome, cpf, senha)
        self.__departamento = departamento
        self.__ramal = ramal