from Usuario import Usuario

class Administrador(Usuario): #Gabriel

    def __init__(self, nome:str, cpf:str, senha:str):

        super().__init__(nome, cpf, senha)