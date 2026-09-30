import re
from validate_docbr import CPF

def cpf_invalido(cpf):
    cpf_validate = CPF()
    return not cpf_validate.validate(cpf)

def name_invalido(name):
    return not nome.isalpha()

def phone_invalido(phone):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model, phone)
    return not response

