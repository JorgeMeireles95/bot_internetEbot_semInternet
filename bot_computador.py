
#bot de computador/PC

# lembra como fará e executa e transgrever com o pyautogui

import pyautogui # executa um comando atras do outro o que pode gerar errp , por isso usa o PAUSE para ter o controle
# abrir  o sistema
pyautogui.PAUSE = 1
pyautogui.press("win")

# Escreve na barra de pesquisa do Windows
pyautogui.write("Login.xlsx")
# Para fazer a pesquisa funcionar
pyautogui.press("backspace")

#entra no programa
pyautogui.press("enter")

import time
time.sleep(10)
#print(pyautogui.position()) # pega a posição



#'''

# Preencher login
pyautogui.click(x=1939, y=266)
pyautogui.write("jorgeantoniomeireles@gmail.com")

# Preencher senha
pyautogui.click(x=1960, y=323)
pyautogui.write("senha")


#Clicar  login
pyautogui.click(x=1867, y=430)





