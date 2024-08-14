option = 0
#---------------------------Declarar Funções------------------------
def showMenu (dictionary):
  for key, value in dictionary.items():
      print(key, value)
    
def sum ():
  a = float(input("Digite o 1º número que deseja somar: "))
  b = float(input("Digite o 2º número que deseja somar: "))
  soma = a + b
  print(f"Resultado é igual a {soma}")

def subtraction ():
  a = float(input("Digite o 1º Número que deseja subtrair: "))
  b = float(input("Digite o 2º Número que deseja subtrair: "))
  sub = a - b
  print(f"Resultado é igual a {sub}")

def multiplication ():
  a = float(input("Digite o 1º Número que deseja multiplicar: "))
  b = float(input("Digite o 2º Número que deseja multiplicar: "))
  multi = a * b
  print(f"Resultado é igual a {multi}")

def division ():
  a = float(input("Digite o 1º Número que deseja dividir: "))
  b = float(input("Digite o 2º Número que deseja dividir: "))
  if b != 0:
    div = a / b
    print(f"Resultado é igual a {div}")
  else: 
    print("Divisão por zero não é permitida")

#-------------------Executar Menu--------------------------
def executeMenu(option):
  if option == "1": 
    print("-" * 80)
    sum ()

  elif option == "2":
    print("-" * 80)
    subtraction()

  elif option == "3":
    print("-" * 80)
    multiplication()

  elif option == "4":
    print("-" * 80)
    division()

  elif option == "5":
    print("Sair da Calculadora")

options = {"1" : "Somar Números",
           "2" : "Subtrair Números",
           "3" : "Muliplicar Números",
           "4" : "Dividir Números",
           "5" : "Sair do Programa"} 

#------------Fluxo Principal-----------------
selected = ""

while selected != "5":
    print("-" * 80)
    showMenu (options)
    print("-" * 80)
    selected = input("Selecione uma opção: ")
    executeMenu(selected)
