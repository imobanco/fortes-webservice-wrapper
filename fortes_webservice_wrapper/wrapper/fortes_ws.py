from ..models.base import TClient, TFornecedor
from .soap import BaseSoapWrapper


class FortesWrapper(BaseSoapWrapper):

    def incluir_cliente(self, cliente):
        data = TClient(**cliente)
        r = self.get_client().service.IncluirClienteComJSON(data.json())
        return r

    def incluir_fornecedor(self, fornecedor):
        data = TFornecedor(**fornecedor)
        r = self.get_client().service.IncluirFornecedorComJSON(data.json())
        return r

    def excluir_cliente(self, document):
        r = self.get_client().service.ExcluiClienteWithCNPJCPF(document)
        return r

    def excluir_fornecedor_com_json(self, fornecedor):
        data = TFornecedor(**fornecedor)
        r = self.get_client().service.ExcluirFornecedorComJSON(data.json())
        return r
