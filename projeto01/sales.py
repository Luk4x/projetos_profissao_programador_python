from dbfread import DBF
from validator import sale_validator
from auto_forms import fill_form

def load_valid_sales():
    sales = DBF("sales.dbf")
    valid_sales = []

    for sale in sales:
        if sale_validator(sale):
            valid_sales.append(sale)

    return valid_sales

sales = load_valid_sales()

for sale in sales:
    print('Preenchendo o formulário de', sale['FULL_NAME'])
    fill_form(sale)

print('Finalizado')