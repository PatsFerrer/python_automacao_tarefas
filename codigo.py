#Importar a biblioteca pyautogui (permite controlar o mouse, teclado e a tela)
# -> pip install pyautogui
# Após isso, você coloca "import pyautogui"
import pyautogui
import time

# instalar pandas <- pip install pandas numpy openpyxl

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escreve um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas. Ex: ctrl + C)

# é importante colocar isso pra não travar, pra nao embolar uma execução na outra
#pausa em CADA UM dos comandos (entre os comandos)
pyautogui.PAUSE = 0.5


# abrir o chrome
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(1)

# Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# entrar no link, 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# espera o site carregar
time.sleep(3)

# Fazer Login
pyautogui.click(x=1030, y=382)
pyautogui.write("email.com")

pyautogui.press("tab") #passei pro campo de senha
pyautogui.write("123")

pyautogui.press("tab") #passei pro botao de login
pyautogui.press("enter")

time.sleep(3)

# Importar a base de dados do produtos
import pandas

tabela = pandas.read_csv("produtos.csv")
# print(tabela)

for linha in tabela.index:

    # Cadastrar 1 produto
    pyautogui.click(x=945, y=271)

    codigo = tabela.loc[linha, "codigo"] #localiza um item de acordo com a [linha, coluna] linha é a variável, a coluna é nome da coluna escrito na tabela

    marca = tabela.loc[linha, "marca"]



    # Preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): # se nao é vazio nossa variavel obs. 'isna' verifica se ta vazio
        pyautogui.write(str(obs))

    #apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(500)
# Repetir o cadastro para todos os produtos
