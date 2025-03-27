# Banco de dados simples para armazenar as médias
media_escola = []

# MENU
def menu():
    while True:
        print("\n====Escolha uma opção====")
        print("1- Calcular média")
        print("2- Listar médias")
        print("3- Sair")
        opcao = input("Digite sua opção: ")

        if opcao == "1":
            calcular_media()
        elif opcao == "2":
            listar_medias()
        elif opcao == "3":
            print("Saindo do programa... Até mais!")
            break
        else:
            print("Opção inválida, por favor escolha uma opção válida.")

# Calcular as médias
def calcular_media(): 
    while True:
        print("=" * 30)
        print("Bem-vindo à calculadora de médias!")
        
        # Entrada do nome e notas
        nome = input("Digite seu nome: ")
        try:
            prova = float(input("Nota da Prova: "))
            teste = float(input("Nota do Teste: "))
            av =  float(input("Nota da Atividade Avaliativa: "))
        except ValueError:
            print("Por favor, insira números válidos para as notas.")
            continue

        # Cálculo da média
        notaf = (2 * prova + teste + av) / 4
        print("-" * 80)
        print(f"{'NOME DO ALUNO':<20} {'NOTA PROVA':<10} {'NOTA TESTE':<10} {'NOTA AV':<10} {'NOTA AFINAL':<10} ")
        print("-" * 80)
        print(f"{nome:<20}  |  {prova:<10.1f}  |  {teste:<10.1f}  |  {av:<10.1f}  |  {notaf:<10.1f} ")

        # Adicionar as notas e a média à lista
        media_escola.append((nome, prova, teste, av, notaf))

        print("=" * 30)
        print("Escolha uma das opções:")
        print("1- Fazer novo cálculo")
        print("2- Voltar ao menu")
        print("3- Sair")
        opcao = input("Digite sua opção: ")

        if opcao == "1":
            continue  # Voltar ao começo do cálculo sem precisar de recursão
        elif opcao == "2":
            return  # Volta ao menu principal
        elif opcao == "3":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida, retornando ao menu principal.")
            break

# Listar as médias
def listar_medias():
    print("=" * 30)
    if len(media_escola) == 0:
        print("Não há médias registradas.")
    else: 
        print("=" * 80)
        print(f"{'NOME DO ALUNO':<20} {'NOTA PROVA':<10} {'NOTA TESTE':<10} {'NOTA AV':<10} {'NOTA AFINAL':<10} ")
        print("-" * 80)

        # Exibir as médias registradas
        for nome, prova, teste, av, notaf in media_escola:
            print(f"{nome:<20}  |  {prova:<10.1f}  |  {teste:<10.1f}  |  {av:<10.1f}  |  {notaf:<10.1f} ")

    print("\nEscolha uma opção:")
    print("1 - Voltar ao menu")
    print("2 - Sair")
    opcao = input("Digite sua opção: ")

    if opcao == "1":
        return  # Voltar ao menu principal
    elif opcao == "2":
        print("Saindo... Até mais!")
        return
    else:
        print("Opção inválida, retornando ao menu principal.")
        return

# Iniciar o menu
menu()
