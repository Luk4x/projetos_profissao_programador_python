from selenium import webdriver

browser = None
def start_browser():
    '''
    apt-get install -yqq unzip
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
    '''
    browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    return browser

def get_browser():
    global browser
    if browser is None:
        browser = start_browser()

    return browser