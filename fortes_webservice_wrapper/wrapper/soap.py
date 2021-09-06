from zeep import Client

from ..constants import WSDL_URL


class BaseSoapWrapper:
    def __init__(self):
        self.wsdl = WSDL_URL

    def get_client(self):
        return Client(self.wsdl)
