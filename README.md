# fortes-webservice-wrapper
Serviço webservice SOAP oferecido pela Fortes para
realizar a criação de clientes e fornecedores.

# Serviços oferecidos via SOAP
- Incluir Cliente
- Incluir Fornecedor
- Excluir Cliente
- Excluir Fornecedor

# Instalação

```angular2html
poetry add fortes-webservice-wrapper
```

# Configuração
- Adicionar `WSDL_URL = urldowebservice` no `.env`
- Importar `from fortes_webservice_wrapper.wrapper.fortes_ws import FortesWrapper`
- Chamar o método que deseja usar

exemplo:
```angular2html
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
    "CampoExtra10": "",
}

FortesWrapper().incluir_cliente(data)
```

# Referências técnicas
- https://docs.python-zeep.org/en/master/
- https://medium.com/@bkaankuguoglu/how-to-send-soap-requests-in-python-using-zeep-9fd78adb5346
- https://medium.com/@ayushi21095/working-with-soap-based-web-service-using-python-8f532195bc6c