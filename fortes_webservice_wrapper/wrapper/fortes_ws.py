defWSDL = 'http://localhost:8000/cgi-bin/agws.exe/wsdl/IAG'
defURL = 'http://localhost:8000/cgi-bin/agws.exe/soap/IAG'
defSvc = 'IAGService'
defPrt = 'IAGPort'

from ..models.base import Client

class TServicosCliente:

    def IncluiClient(self, Client:Client):
        pass

    def GetClientWithIdentificador(self, id):
        pass
