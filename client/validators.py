import re
from validate_docbr import CPF


def cpf_valido(numero_do_cpf):
    # Validar CPF
    cpf = CPF()
    return  cpf.validate(numero_do_cpf)  # True

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9 

def celular_valido(numero_celular):
    """Verifica se o celular é valido (19 99999-9999)"""
    modelo ='[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,numero_celular)
    return resposta


            
        
           
        
        
    