#Cadastro
def cadatrarVazamento(emailLeak):
    resposta = "S"
    while resposta == "S":
        tag = input("\nQual TAG gostaria de dar ao vazamento? ")
        emailLeak[tag]=[input("Qual e-mail vazou? ").upper(), input("Qual senha foi vazada para o e-mail? ").upper()]
        resposta = input("Gostaria de cadastrar mais algum vazamento?(S/N) ").upper()

#Mostrar Leaks cadastrados
def vazamentoCadastrado(emailLeak):
    for tag, dados in emailLeak.items():
        print("\nTAG............: ", tag)
        print("E-mail e Senha.: ", dados)

#Procurar por um Leak
def buscarVazamento(emailLeak):
    busca=input("\nQual a sua tag do seu vazamento? ")
    lista = emailLeak.get(busca)
    if lista != None:
        print("Email Vazado...: ", lista[0])
        print("Senha Vazada...: ", lista[1])
    else:
        print("Vazamento não encontrado. ")


#Deletar Vazamento
#def deletarVazamento(emailLeak):
#    deletar = input("Qual vazamento gostaria de excluir? ")
#    if emailLeak.get(deletar) != None:    
#        del emailLeak(deletar)
#    print("Vazamento excluido.\n")