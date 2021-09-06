from ..constants import WSDL_URL
from ..models.base import TClient, TFornecedor
from .soap import BaseSoapWrapper


class FortesWrapper(BaseSoapWrapper):

    # def trata_retorno(self, data):
    #     mensagem_retorno = data.find("Retorno")
    #     mensagem_erro = data.find("Erro")
    #
    #     mensagem_retorno = data[mensagem_retorno:mensagem_erro]
    #     mensagem_erro = data[mensagem_erro:]
    #
    #     return mensagem_retorno, mensagem_erro

    def _get_wsdl(self):
        return self.get_client(WSDL_URL)

    def incluir_cliente(self, cliente):
        data = TClient(**cliente)
        r = self._get_wsdl().service.IncluirClienteComJSON(data.json())
        return r

    def incluir_fornecedor(self, fornecedor):
        data = TFornecedor(**fornecedor)
        r = self._get_wsdl().service.IncluirFornecedorComJSON(data.json())
        return r

    def excluir_cliente(self, document):
        r = self._get_wsdl().service.ExcluiClienteWithCNPJCPF(document)
        return r

    def excluir_fornecedor_com_json(self, fornecedor):
        data = TFornecedor(**fornecedor)
        r = self._get_wsdl().service.ExcluirFornecedorComJSON(data.json())
        return r
