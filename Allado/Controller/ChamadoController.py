from Model.Chamado import Chamado
from Model.classe_suporte import Documento, Categoria, Comentario, Prioridade, Status
from Model.Usuarios import Pac, Tecnico
from View.ChamadoView import ChamadoView

class ControllerChamado:

    def __init__(self):
        self.__lista_chamados = []
        self.__chamado_view = ChamadoView()
        self.__chamado_view.DefineController(self)

    def AbreChamado (self,
                     titulo:str,
                     descricao:str,
                     prioridade: Prioridade,
                     categoria: Categoria):
        id_chamado = len(self.__lista_chamados)+1
        new_chamado = Chamado(id_chamado,
                              titulo,
                              descricao,
                              status="ABERTO",
                              prioridade="BAIXA",
                              categoria="ESCOLHER")
        self.__lista_chamados.append(new_chamado)
        return id_chamado

    def AdicionaComentario (self,
                            id_chamado:int,
                            comentario: str):
        if self.VerificaChamadoExiste() and comentario is not None:
            self.__comentario = comentario
        else:
            raise ValueError

    def AdicionaDocumento (self,
                           id_chamado:int,
                           documento:Documento):
        if self.VerificaChamadoExiste(id_chamado):
            chamado = self.__lista_chamados[id_chamado]
            self.__documento = documento
        else:
            raise ValueError

    def AlteraCategoria (self,
                        id_chamado:int,
                        categoria: Categoria):
        if self.VerificaChamadoExiste(id_chamado):
            chamado = self.GetChamado(id_chamado)
            chamado.categoria.setter(categoria)
        else:
            raise ValueError

    def AlteraPrioridade (self,
                          id_chamado:int,
                          prioridade:Prioridade):
        if self.VerificaChamadoExiste(id_chamado):
            chamado = self.GetChamado(id_chamado)
            chamado.prioridade.setter(prioridade)
        else:
            raise ValueError

    def AlteraResponsavel (self,
                           id_chamado:int,
                           responsavel:Tecnico):
        if self.VerificaChamadoExiste(id_chamado):
            chamado = self.GetChamado(id_chamado)
            chamado.responsavel.setter(responsavel)
        else:
            raise ValueError

    def AlteraSala (self,
                    id_chamado:int,
                    sala:str):
        if self.VerificaChamadoExiste(id_chamado):
            chamado = self.getchamado(id_chamado)
            chamado.sala.setter(sala)
        else:
            raise ValueError

    def AlteraSolicitante(self,
                          id_chamado:int,
                          solicitante:Pac):
        if self.VerificaChamadoExiste(id_chamado):
            chamado = self.GetChamado(id_chamado)
            chamado.solicitante.setter(solicitante)
        else:
            raise ValueError

    def AlteraStatus(self,
                     id_chamado:int,
                     status:Status):
        if self.VerificaChamadoExiste(id_chamado):
            chamado = self.GetChamado(id_chamado)
            chamado.status.setter(status)
        else:
            raise ValueError

    def ExcluiChamado(self,
                      id_chamado:int):
        if self.VerificaChamadoExiste(id_chamado):
            chamado = self.__lista_chamados.index(self.GetChamado(id_chamado))
            self.__lista_chamados.pop[chamado]
        else:
            raise ValueError

    def VerificaChamadoExiste(self,
                              id_chamado:int):
        for i in range(self.__lista_chamados):
            if i.GetId == id_chamado:
                 return True
            else:
                 return False

    def GetChamado (self,
                    id_chamado:int):
        if self.VerificaChamadoExiste():
            for c in range(self.__lista_chamados):
                if c.GetId == id_chamado:
                    return c
        else:
            raise ValueError

    def ListaChamados(self):
        return self.__lista_chamados