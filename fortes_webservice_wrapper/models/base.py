from pydantic import BaseModel, constr
from typing import Literal, Optional, Union

class Client(BaseModel):
    """Informação de Cliente"""
    codigo: str
    nome: str
    nomeFantasia: str
    cnpjcpf: str
    cep: str
    logradouro: str
    bairro: str
    numero:str
    complemento: str
    uf:str
    cidade: str
    ddd: str
    fone:str
    fax: str
    identificador: str
    celular:str
    email: str
    contato: str
    site: str
    rg:str
    ie: str
    grupo:str
    agenteCobrador:str
    receita:str
    contaContabil: str
    Representante:str
    Vencimento: str
    Etiqueta: str
    GeraNFAuto: str
    RetemINSS: str
    AliquotaISS: str
    IM: str
    CampoExtra1: str
    CampoExtra2:str
    CampoExtra3: str
    CampoExtra4: str
    CampoExtra5: str
    CampoExtra6: str
    CampoExtra7: str
    CampoExtra8: str
    CampoExtra9: str
    CampoExtra10: str
    Exterior: str
    Inseto_de_IE: str