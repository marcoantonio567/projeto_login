from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import openpyxl

# configure firefox options
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)


# define url
url = "http://127.0.0.1:5000"

# load excel file
workbook = openpyxl.load_workbook('produtos.xlsx')
vendas_sheet = workbook['Sheet']


#get url page
driver.get(url)

#join login form
driver.find_element(By.XPATH,'/html/body/form/div/input[1]').send_keys('saitama')
driver.find_element(By.XPATH,'/html/body/form/div/input[2]').send_keys('1234')
driver.find_element(By.XPATH,'/html/body/form/button').click()


for row in vendas_sheet.iter_rows(min_row=2):
    #access form and fill it by xpath
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[1]/input').send_keys(row[0].value)
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[2]/input').send_keys(row[1].value)
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[3]/input').send_keys(row[2].value)
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[4]/input').send_keys(row[3].value)
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[5]/input').send_keys(row[4].value)
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[6]/input').send_keys(row[5].value)
    driver.find_element(By.XPATH, '/html/body/main/form/div/div[7]/input').send_keys(row[6].value)
    driver.find_element(By.XPATH, '/html/body/main/form/div/button').click()


