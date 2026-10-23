from datetime import datetime
from Model.classe_suporte import Documento
from Usuarios.Pac import Pac
from Usuarios.Tecnico import Tecnico
from classe_suporte import Avaliacao, Categoria,\
                            Comentario, Prioridade, Status

class Chamado: #Gabriel

    def __init__(self,
                id_chamado:int,
                titulo:str,
                descricao:str,
                status:Status,
                prioridade:Prioridade,
                categoria:Categoria,
                sala:str,
                tecnico_responsavel:Tecnico,
                solicitante:Pac):

    #área de informação do chamado
        self.__id_chamado = id_chamado
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_abertura = datetime.now()
        self.__data_fechamento = None
        self.__comentario = None
        self.__anexos = None

    #área de controle do chamado
        self.__status = status
        self.__prioridade = prioridade
        self.__categoria = categoria
        self.__sala = sala

    #envolvidos no chamado
        self.__responsavel = tecnico_responsavel
        self.__solicitante = solicitante

    @comentario.setter
    def AdicionarComentario (self,
                            comentario:str):
        self.__comentario = comentario

    @categoria.setter
    def AlteraCategoria (self,
                        categoria:Categoria):
        self.__categoria = categoria

    @prioridade.setter
    def AlteraPrioridade (self,
                          prioridade:Prioridade):
        self.__prioridade = prioridade

    @responsavel.setter
    def AlteraResponsavel (self,
                           responsavel:Tecnico):
        self.__tecnico = responsavel

    @sala.setter
    def AlteraSala (self,
                    sala:str):
        self.__sala = sala

    @solicitante.setter
    def AlteraSolicitante (self,
                           solicitante:Pac):
        self.__solicitante = solicitante

    @status.setter
    def AlteraStatus (self,
                      status:Status):
        self.__status = status

    @property
    def GetId (self):
        return self.__id_chamado
    