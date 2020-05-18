from funcoes import *

email = {"caiodm088":["caiodm088@gmail.com", "123456"], "rm85590":["rm85590@fiap.com.br", "password"]}


while True:
    print("\nCadastrar vazamento(1) ")
    print("Verificar vazamentos cadastrados(2) ")
    print("Procurar algum vazamento(3) ")
    print("Para sair (0)")
    opcao = input("Qual opção gostaria de escolher? ")
    if opcao == "1":
        cadatrarVazamento(email)
    elif opcao == "2":
        vazamentoCadastrado(email)
    elif opcao == "3":
        buscarVazamento(email)
    elif opcao == "0":
        break
    else:
        print("OPÇÃO INVALIDA!") 
        
    
    