'''
FULL_NAME = Nome completo
EMAIL = Email
SOURCE = atacado ou varejo
CATEGORIES = Produtos: "Camisa","Calça", "Vestido", "Roupas Íntimas"
TYPE = Tipo da conta: "Não Cadastrado", "Cadastrado", "Cliente Regular", "Cliente Premium"
RATING = Nota avaliativa: Número [1-5]
'''
import re

def name_validator(name):
    # https://stackoverflow.com/questions/2385701/regular-expression-for-first-and-last-name
    pattern = r"^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$"
    valid_name = re.match(pattern, name)
    return valid_name is not None

def email_validator(email):
    pattern = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    valid_email = re.match(pattern, email)
    return valid_email is not None

def source_validator(source):
    valid_sources = ['Atacado', 'Varejo']

    if source in valid_sources:
        return True
    else:
        return False

def categories_validator(categories):
    valid_categories = ['Camisa', 'Calça', 'Vestido', 'Roupas Íntimas']

    for category in categories.split(', '):
        if category not in valid_categories:
            return False

    return True

def account_type_validator(account_type):
    valid_account_types = ['Não Cadastrado', 'Cadastrado', 'Cliente Regular', 'Cliente Premium']

    return account_type in valid_account_types

def rating_validator(rating):
    pattern = r'^[1-5]$'
    valid_rating = re.match(pattern, rating)
    return valid_rating is not None

def sale_validator(sale):
    name = sale['FULL_NAME']
    email = sale['EMAIL']
    source = sale['SOURCE']
    categories = sale['CATEGORIES']
    account_type = sale['TYPE']
    rating = sale['RATING']
    
    return (
        name_validator(name)
        and email_validator(email)
        and source_validator(source)
        and categories_validator(categories)
        and account_type_validator(account_type)
        and rating_validator(rating)
    )