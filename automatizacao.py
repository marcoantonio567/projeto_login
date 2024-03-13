from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Configurando as opções do Firefox
options = webdriver.FirefoxOptions()
# Criando o driver do Firefox
driver = webdriver.Firefox(options=options)


# Definindo a URL do Google
url = "http://127.0.0.1:5000"

# Acessando a URL do Google
driver.get(url)

#entrar no link acima pegar o email e a senha e digitar depois apertar entrar 
driver.find_element(By.XPATH,'/html/body/form/div/input[1]').send_keys('saitama')
driver.find_element(By.XPATH,'/html/body/form/div/input[2]').send_keys('1234')
driver.find_element(By.XPATH,'/html/body/form/button').click()
