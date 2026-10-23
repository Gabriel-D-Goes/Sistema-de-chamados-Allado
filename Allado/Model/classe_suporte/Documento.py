class Documento: #Gabriel

    def __init__(self, documento):
        self.__documento = documento

    @property
    def documento (self):
        return self.__documento

    @documento.setter
    def documento (self, documento):
        self.__documento = documento
    