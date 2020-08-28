import schedule
import time
from selenium import webdriver
from selenium.webdriver import Firefox
import msedge

driver = webdriver.Firefox(executable_path=r'./geckodriver.exe')
driver.implicitly_wait(5)

def loginbaterponto():    
    name_login = 'usuario'
    name_senha = 'senha'
    id_btn = 'login'
    login = '61047049'
    senha = 'alex@123'
    btnid = "login"
    driver.get('https://pontosecullum4-02.secullum.com.br/ponto4web/1508660410#cartao-ponto')
    input_login = driver.find_element_by_name(name_login)   
    input_senha = driver.find_element_by_name(name_senha)   
    btn_login = driver.find_element_by_id(btnid)
    input_login.send_keys(login)
    input_senha.send_keys(senha)
    btn_login.click()
    
    driver.get('https://pontosecullum4-02.secullum.com.br/ponto4web/1508660410#batidas-manuais')
    id_btnresgistrar = "registrar"
    btn_registro = driver.find_elements_by_id(id_btnresgistrar)
    btn_registro.click()

loginbaterponto() 

#teste
#schedule.every().monday.at("08:00","12:00","13:00","18:00").do(loginbaterponto)
#schedule.every().tuesday.at("08:00","12:00","13:00","18:00").do(loginbaterponto)
#schedule.every().wednesday.at("08:00","12:00","13:00","18:00").do(loginbaterponto)
#schedule.every().thursday.at("08:00","12:00","13:00","18:00").do(loginbaterponto)
#schedule.every().friday.at("08:00","12:00","13:00","17:00").do(loginbaterponto)








