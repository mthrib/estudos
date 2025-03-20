def macas():
    while True:
        maca = int(input("Quantas unidades de maçã vão ser compradas? "))
        
        if maca < 12:
           valor_final1 = maca * 1.30
           print("===================")
           print(f"Valor final = R$ {valor_final1:.1f}")
           break
        else:
            valor_final2 = maca * 1
            print("===================")
            print(f"Valor final = R$ {valor_final2:.1f}")
            break
        
def bananas():
    while True:
        banana = int(input("Quantos cachos de banana vão ser comprados?"))
        if banana <= 3:
            valor1 = banana * 4.69
            print("==============================")
            print(f"Valor final = R$ {valor1:.1f}")
            break
        else:
            valor2 = banana * 3.49
            print("==============================")
            print(f"Valor final = R$ {valor2:.1f}")
            break
    
def menu():
    while True:
        print("\n____MENU____")
        print("1 - Calculo maçãs")
        print("2 - Calculo de bananas")
        print("3 - sair")
        
        opcao = (input("Digite sua opção: "))
            
        if opcao == "1":
            macas()
        elif opcao == "2":
            bananas()
        elif opcao == "3":
            break
        else:
            print("Você digitou um valor inválido")

menu()
