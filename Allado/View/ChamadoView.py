from Controller import ChamadoController
from Model.classe_suporte import Prioridade, Categoria, Documento, Comentario, Status
from Model.Usuarios import Pac, Tecnico

class ChamadoView:

    def __init__(self):
        self.__usuario_atual = None
        self.__chamado_controller = None

    def ListaChamados(self):
        self.chamado_controller.ListaChamados()

    def MostraChamado(self,
                      id_chamado:int):
        chamado = self.__chamado_controller.GetChamado(id_chamado)
        return chamado

    def NewChamado (self,
                    titulo:str,
                    descricao:str,
                    prioridade: Prioridade,
                    categoria: Categoria):
        self.__chamado_controller.AbreChamado(titulo,
                                              descricao,
                                              prioridade,
                                              categoria)

    def NewComentario (self,
                       id_chamado:int,
                       comentario: Comentario):
        self.__chamado_controller.AdicionaComentario(comentario)

    def NewDocumento (self,
                      id_chamado:int,
                      documento: Documento):
        self.__chamado_controller.AdicionaDocumento(documento)

    def SeletorCategoria(self,
                         id_chamado:int,
                         categoria: Categoria):
        self.__chamado_controller.AlteraCategoria(categoria)

    def SeletorPrioridade(self,
                          id_chamado:int,
                          prioridade: Prioridade):
        self.__chamado_controller.AlteraPrioridade(prioridade)

    def SeletorResponsavel(self,
                           id_chamado:int,
                           responsavel: Tecnico):
        self.__chamado_controller.AlteraResponsavel(responsavel)

    def SeletorSolicitante(self,
                           id_chamado:int,
                           solicitante: Pac):
        self.__chamado_controller.AlteraSolicitante(solicitante)

    def seletorStatus (self,
                       id_chamado:int,
                       status: Status):
        self.__chamado_controller.AlteraStatus(status)
        
    def MensagemErro(self):
        pass

    def MensagemSucesso(self):
        pass

    def DefineController (self,
                          controller:ChamadoController):
        self.__chamado_controller = controller