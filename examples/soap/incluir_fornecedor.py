from fortes_webservice_wrapper.wrapper.fortes_ws import FortesWrapper

fornecedor = {
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
                    "ServicoPublico": "",
                    "ICMS": "",
                    "IPI": ""
        }

r = FortesWrapper().incluir_fornecedor(fornecedor)

