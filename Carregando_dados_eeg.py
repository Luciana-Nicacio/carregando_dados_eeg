#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 18:27:23 2025

@author: luciana
"""
import numpy as np
import matplotlib.pyplot as py
from os import chdir, getcwd, listdir,mkdir, system
import datetime as dt
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askdirectory

dir_atual = getcwd()
data = dt.datetime.now()
py.close('all')

tipo_estimulo = 'estimulo1' #ou 'estimulo3'


if tipo_estimulo == 'estimulo1':
    estimulacao = 'Estimulação senoidal'
if tipo_estimulo == 'estimulo3':
    estimulacao = 'Estimulação musical'

#%% Carregando os dados
root = Tk()
root.withdraw()
diretorio_dados = askdirectory(title = 'Escolha o diretório do bando de dados de EEG')

chdir(diretorio_dados)
Dados = pd.read_pickle('Dados_originais_%s.txt'%tipo_estimulo) #carrega dicionário com os dados de todos os voluntários. Cada voluntário ID possui os seguintes os seguintes dados:['EEG', 'Perguntas', 'Respostas', 'Delays'] 

#%% Selecionando diretorio de dados
canais = ['F7','T3','T5','Fp1','F3','C3','P3','O1','F8','T4','T6','Fp2','F4','C4','P4','O2','Fz','Cz','Pz','Oz','A1','A2','Am'] #canal Am não foi coletado. Ele será criado pela média de A1 e A2

n_canais = list(range(len(canais)))

c_ref = 17 #canal Cz
fs=601.5
fmod = [53*fs*0.9999652354427383/1024,67*fs*0.9999652354427383/1024] #31,13Hz(esquerda) e 39,36Hz (direita)   
Nx = 1024*3 #tamanha da janela em que ocorreu a estimulação 


voluntarios = list(range(32,54)) #[x for x in range(32,54) if x not in [40,41]]: #exclui o voluntário 41 que dormiu no 2º teste    

print('Itens do banco de dados:',list(Dados))
print('\nTipo de estímulo utilizado no experimento: %s = %s'%(Dados['estimulo'],estimulacao))
print('\nPara cada voluntário, existem os seguintes dados:', list(Dados['ID32']))
print('\nPara o voluntário ID32, por exemplo, foram realizadas as seguintes perguntas do questionário: ',list(Dados['ID32']['Perguntas']))
print('\nAs respostas do ID32 para as perguntas foram: ',Dados['ID32']['Respostas'])
print('\nDelay é o intervalo de tempo entre o início da coleta dos sinais de EEG e o início da estimulação. O delay de cada ensaio, em segundos, para ID32 é: ',Dados['ID32']['Delays'])

