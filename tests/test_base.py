from unittest import TestCase

from fortes_webservice_wrapper.models.base import TClient, TFornecedor


class BaseModelsTestCase(TestCase):
    def test_cliente(self):
        data = {
            "codigo": "",
            "nome": "Ana do Imobanco",
            "nomeFantasia": "ImoAna",
            "cnpjcpf": "57632889043",
            "cep": "60015140",
            "logradouro": "Rua Teresa Cristina",
            "bairro": "Centro",
            "numero": "",
            "complemento": " ",
            "uf": "CE",
            "cidade": "04400",
            "ddd": "",
            "fone": "",
            "fax": "",
            "identificador": "",
            "celular": "",
            "email": "",
            "contato": "",
            "site": "",
            "rg": "",
            "ie": "",
            "grupo": "0001",
            "agenteCobrador": "",
            "receita": "",
            "contaContabil": "",
            "Representante": "",
            "Vencimento": 10,
            "Etiqueta": 0,
            "GeraNFAuto": 0,
            "RetemISS": 0,
            "RetemINSS": 0,
            "AliquotaISS": 0,
            "IM": "",
            "CampoExtra1": "",
            "CampoExtra2": "",
            "CampoExtra3": "",
            "CampoExtra4": "",
            "CampoExtra5": "",
            "CampoExtra6": "",
            "CampoExtra7": "",
            "CampoExtra8": "",
            "CampoExtra9": "",
            "CampoExtra10": ""
        }
        result = TClient(**data)
        expected = '{"codigo": "", "nome": "Ana do Imobanco", "nomeFantasia": "ImoAna", "cnpjcpf": "57632889043", "cep": "60015140", "logradouro": "Rua Teresa Cristina", "bairro": "Centro", "numero": "", "complemento": " ", "uf": "CE", "cidade": "04400", "ddd": "", "fone": "", "fax": "", "identificador": "", "celular": "", "email": "", "contato": "", "site": "", "rg": "", "ie": "", "grupo": "0001", "agenteCobrador": "", "receita": "", "contaContabil": "", "Representante": "", "Vencimento": 10, "Etiqueta": 0, "GeraNFAuto": 0, "RetemINSS": 0, "AliquotaISS": "0", "IM": "", "CampoExtra1": "", "CampoExtra2": "", "CampoExtra3": "", "CampoExtra4": "", "CampoExtra5": "", "CampoExtra6": "", "CampoExtra7": "", "CampoExtra8": "", "CampoExtra9": "", "CampoExtra10": "", "Exterior": null, "Inseto_de_IE": null}'
        self.assertEqual(result.json(), expected)

    def test_fornecedor(self):
        data = {
            "Codigo": "",
            "Nome": "Ana do Imobanco",
            "CNPJCPF": "31510515020",
            "CEP": "",
            "Logradouro": "",
            "Bairro": "",
            "Numero": "",
            "Complemento": "",
            "UF": "",
            "Cidade": "",
            "DDD": "",
            "Fone": "",
            "Fax": "",
            "Email": "",
            "Contato": "",
            "Site": "",
            "RG": "",
            "IE": "",
            "Grupo": "",
            "Receita": "",
            "IM": "",
            "Referencia": "",
            "FinalidadeTED": "",
            "FinalidadeDOC": "",
            "Celular": "",
            "Leiaute": "",
            "Banco": "",
            "BancoNumero": "",
            "Agencia": "",
            "CC": "",
            "DVAg": "",
            "DVCC": "",
            "ServicoPublico": 0,
            "ICMS": 0,
            "IPI": 0
        }
        result = TFornecedor(**data)
        expected = '{"Codigo": "", "Nome": "Ana do Imobanco", "CNPJCPF": "31510515020", "CEP": "", "Logradouro": "", "Bairro": "", "Numero": "", "Complemento": "", "UF": "", "Cidade": "", "DDD": "", "Fone": "", "Fax": "", "Email": "", "Contato": "", "Site": "", "RG": "", "IE": "", "Grupo": "", "Receita": "", "IM": "", "Referencia": "", "FinalidadeTED": "", "FinalidadeDOC": "", "Celular": "", "Leiaute": "", "Banco": "", "BancoNumero": "", "Agencia": "", "CC": "", "DVAg": "", "DVCC": "", "ServicoPublico": 0, "ICMS": 0, "IPI": 0}'
        self.assertEqual(result.json(), expected)
