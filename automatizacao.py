from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import openpyxl

# Configurando as opções do Firefox
options = webdriver.FirefoxOptions()
# Criando o driver do Firefox
driver = webdriver.Firefox(options=options)


# Definindo a URL do Google
url = "http://127.0.0.1:5000"

#carregando a planilha excel
workbook = openpyxl.load_workbook('produtos.xlsx')
vendas_sheet = workbook['Sheet']


# Acessando a URL do Google
driver.get(url)

#entrar no link acima pegar o email e a senha e digitar depois apertar entrar 
driver.find_element(By.XPATH,'/html/body/form/div/input[1]').send_keys('saitama')
driver.find_element(By.XPATH,'/html/body/form/div/input[2]').send_keys('1234')
driver.find_element(By.XPATH,'/html/body/form/button').click()


for linha in vendas_sheet.iter_rows(min_row=2):
    #acessando o formulario e preenchendo ele 
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[1]/input').send_keys(linha[0].value)
    #id
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[2]/input').send_keys(linha[1].value)
    #nome
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[3]/input').send_keys(linha[2].value)
    #categoria
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[4]/input').send_keys(linha[3].value)
    #preço
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[5]/input').send_keys(linha[4].value)
    #quantidade
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[6]/input').send_keys(linha[5].value)
    #fabricante
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[7]/input').send_keys(linha[6].value)
    #chegada
    driver.find_element(By.XPATH, '/html/body/main/form/div/button').click()
    #clica no botão de enviar

