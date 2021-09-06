from zeep import Client


class BaseSoapWrapper:
    def get_client(self, wsdl):
        return Client(wsdl)
