#menu
def menu():
    print("____MENU_____")
    print("1 - Fazer Um Novo Cálculo")    
    print("2 - Sair")

#Seja Bem_Vindo
def calculo():

    #Pergunta e Comnta
    while True:
        valor = float(input("Valor do Produto: R$"))
        desconto = float(input("Valor do Desconto: (%)"))

        if 0 <= desconto <= 100:
            valor_final = valor * (1 - desconto / 100)
            print("|Valor do Produto: R$", valor, "|Valor do Desconto:", desconto, "%", "|Seu Valor Final Vai Ser: R$", valor_final)
            break
        else:
            print("Desconto Inválido! Digite Um Valor Entre 0 e 100")
    

        opcao = input("Digite Sua Opção: ")

        if opcao == "2":
            print("Obrigado Por Usar a Calculadora! Saindo")
            print("Obrigado Por Usar a Calculadora! Saindo .")
            print("Obrigado Por Usar a Calculadora! Saindo ..")
            print("Obrigado Por Usar a Calculadora! Saindo ...")
            break
        elif opcao == "1":
            calculo()
        else:
            print("Opcção Inválida! Tente Novamente")
            menu()
            

           

print("Seja Bem-Vindo(a)!")
print("==================")
calculo()
menu()        
