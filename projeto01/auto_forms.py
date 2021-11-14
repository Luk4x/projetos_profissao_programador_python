import time
from browser import get_browser

def load_form():
    get_browser().get("https://forms.gle/rKfhMRdiE7qRjMK38")
    time.sleep(3)

def fill_name(name):
    element = get_browser().find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    element.send_keys(name)

def fill_email(email):
    element = get_browser().find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    element.send_keys(email)

def fill_source(source):
    if source == 'Atacado':
        opt = 1
    else:
        opt = 2
    element = get_browser().find_element_by_xpath(f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[{opt}]/label/div/div[1]/div/div[3]/div")
    element.click()

def fill_categories(categories):
    for category in categories.split(", "):
        if category == "Camisa":
            opt = 1
        elif category == "Calça":
            opt = 2
        elif category == "Vestido":
            opt = 3
        else:
            opt = 4

        get_browser().find_element_by_xpath(f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[{opt}]/label/div/div[1]/div[2]").click()

def fill_account_type(account_type):
    get_browser().find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]").click() # open account type form options
    time.sleep(2)
    
    if account_type == "Não Cadastrado":
        opt = 3
    elif account_type == "Cadastrado":
        opt = 4
    elif account_type == "Cliente Regular":
        opt = 5
    else:
        opt = 6

    element = get_browser().find_element_by_xpath(f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[{opt}]/span")
    element.click()
    element.click()

def fill_rating(rating):
    element = get_browser().find_element_by_xpath(f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[{rating}]/div[2]/div/div/div[3]/div")
    element.click()

def send_form():
    get_browser().find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()

def fill_form(sale):
    time.sleep(1)
    load_form()
    name = sale['FULL_NAME']
    email = sale['EMAIL']
    source = sale['SOURCE']
    categories = sale['CATEGORIES']
    account_type = sale['TYPE']
    rating = sale['RATING']
    time.sleep(1)
    fill_name(name)
    time.sleep(1)
    fill_email(email)
    time.sleep(1)
    fill_source(source)
    time.sleep(1)
    fill_categories(categories)
    time.sleep(1)
    fill_account_type(account_type)
    time.sleep(2)
    fill_rating(rating)
    time.sleep(1)
    send_form()

