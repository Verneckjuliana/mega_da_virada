import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd


class Web:
    def __init__(self):
        self.link = 'https://asloterias.com.br/resultados-da-mega-sena-2022?ordenacao=crescente'
        self.map = {
            'numeros': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/span[$NUM$]'
            },
            'concurso': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/strong[$NUM$]'
            }
        }

        self.driver = webdriver.Chrome()

    def abrir_site(self):
        self.driver.get(self.link)
        sleep(2)
        global df, numero, i
        jogo = []
        matriz = []
        k = 0
        for j in range(1, 111):
            for i in range(6):
                k += 1
                if self.driver.find_element(By.XPATH, self.map['numeros']['xpath'].replace('$NUM$', f'{k}')).text != 'Mega da Virada':
                    j += 1
                    i = 0
                else:
                    numero = self.driver.find_element(By.XPATH, self.map['numeros']['xpath'].replace('$NUM$', f'{k}')).text
                jogo.append(numero)
            matriz.append(jogo)
            jogo = []

        for w in range(len(matriz)):
            print('')
            for l in range(6):
                print(matriz[w][l], end='\t')

            planilha = pd.DataFrame(matriz)
            planilha.to_excel('C:/Users/40428576800/Desktop/planilha_gerada.xlsx')




