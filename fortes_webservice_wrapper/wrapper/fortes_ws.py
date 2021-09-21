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

    # def listar_clientes(self):
    #   Não está funcionando
    #     import pdb; pdb.set_trace()
    #     r = self.get_client().service.getListaClientes(False, '', False)
    #     return r

    def listar_fornecedores(self):
        r = self.get_client().service.getListaFornecedores()
        return r

    def alterar_cliente(self, cliente):
        data = TClient(**cliente)
        r = self.get_client().service.AlterarClienteComJSON(data.json())
        return r

    def alterar_fornecedor(self, fornecedor):
        data = TClient(**fornecedor)
        r = self.get_client().service.AlterarFornecedorComJSON(data.json())
        return r

    def buscar_cliente(self, document):
        import pdb; pdb.set_trace()
        r = self.get_client().service.getObjetoClienteWithCPFCNPJ(document)
        return r

    def buscar_fornecedor(self, document):
        r = self.get_client().service.GetFornecedorWithCPFCNPJ(document)
        return r
