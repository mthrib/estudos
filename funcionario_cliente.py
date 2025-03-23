# Listas para armazenar funcionários e clientes
funcionarios = []
clientes = []

# Contadores para IDs
contador_idf = 1
contador_idc = 1

# Função para exibir o menu
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar Funcionário")
        print("2 - Cadastrar Cliente")
        print("3 - Lista de Funcionários")
        print("4 - Lista de Clientes")
        print("5 - Buscar Funcionário por ID")
        print("6 - Buscar Cliente por ID")
        print("7 - Sair")
        
        opcao = input("Digite sua opção: ")
        
        if opcao == "1":
            cadastrar_funcionarios()
        elif opcao == "2":
            cadastrar_clientes()
        elif opcao == "3":
            listar_funcionarios()
        elif opcao == "4":
            listar_clientes()
        elif opcao == "5":
            buscar_funcionario_por_id()
        elif opcao == "6":
            buscar_cliente_por_id()
        elif opcao == "7":
            print("Saindo do programa...")
            break
        else:
            print("ERRO: Você digitou uma opção inválida!")

# Função para cadastrar funcionários
def cadastrar_funcionarios():
    global contador_idf  # Usando a variável global para ID único
    
    funcionario_id = contador_idf
    contador_idf += 1  # Incrementa o ID para o próximo cadastro
    
    funcionario = input("Nome do funcionário: ")
    aniversario_funcionario = input("Data de nascimento: ")
    endereco_funcionario = input("Qual seu endereço: ")
    
    # Adiciona o funcionário à lista
    funcionarios.append({
        "ID": funcionario_id,
        "Nome": funcionario,
        "Nascimento": aniversario_funcionario,
        "Endereço": endereco_funcionario
    })

    print(f"\nFuncionário cadastrado com sucesso! ID: {funcionario_id}")

# Função para cadastrar clientes
def cadastrar_clientes():
    global contador_idc  # Usando a variável global para ID único
    
    cliente_id = contador_idc
    contador_idc += 1  # Incrementa o ID para o próximo cadastro
    
    cliente = input("Nome do cliente: ")
    aniversario_cliente = input("Data de nascimento: ")
    endereco_cliente = input("Qual seu endereço: ")
    
    # Adiciona o cliente à lista
    clientes.append({
        "ID": cliente_id,
        "Nome": cliente,
        "Nascimento": aniversario_cliente,
        "Endereço": endereco_cliente
    })

    print(f"\nCliente cadastrado com sucesso! ID: {cliente_id}")

# Função para listar funcionários
def listar_funcionarios():
    if not funcionarios:
        print("\nNenhum funcionário cadastrado.")
    else:
        print("\n--- Lista de Funcionários ---")
        for func in funcionarios:
            print(f"ID: {func['ID']} | Nome: {func['Nome']} | Nascimento: {func['Nascimento']} | Endereço: {func['Endereço']}")

# Função para listar clientes
def listar_clientes():
    if not clientes:
        print("\nNenhum cliente cadastrado.")
    else:
        print("\n--- Lista de Clientes ---")
        for cli in clientes:
            print(f"ID: {cli['ID']} | Nome: {cli['Nome']} | Nascimento: {cli['Nascimento']} | Endereço: {cli['Endereço']}")

# Função para buscar funcionário pelo ID
def buscar_funcionario_por_id():
    if not funcionarios:
        print("\nNenhum funcionário cadastrado.")
        return

    try:
        id_procurado = int(input("Digite o ID do funcionário: "))
    except ValueError:
        print("\nERRO: Digite um número válido.")
        return
    
    for func in funcionarios:
        if func["ID"] == id_procurado:
            print("\n--- Funcionário Encontrado ---")
            print(f"ID: {func['ID']} | Nome: {func['Nome']} | Nascimento: {func['Nascimento']} | Endereço: {func['Endereço']}")
            return
    
    print("\nFuncionário não encontrado.")

# Função para buscar cliente pelo ID
def buscar_cliente_por_id():
    if not clientes:
        print("\nNenhum cliente cadastrado.")
        return

    try:
        id_procurado = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("\nERRO: Digite um número válido.")
        return
    
    for cli in clientes:
        if cli["ID"] == id_procurado:
            print("\n--- Cliente Encontrado ---")
            print(f"ID: {cli['ID']} | Nome: {cli['Nome']} | Nascimento: {cli['Nascimento']} | Endereço: {cli['Endereço']}")
            return
    
    print("\nCliente não encontrado.")

# Inicia o programa
menu()
