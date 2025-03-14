def obter_nota(mensagem):
    while True:  # "True" com "T" maiúsculo
        try:
            nota = float(input(mensagem))  # "=" ao invés de "-"
            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: A nota deve estar entre 0 e 10. Tente novamente!")
        except ValueError:
            print("ERRO: Insira um valor válido.")

# Dados
nome = input("Nome do aluno: ")
notaprova = obter_nota("Qual sua nota da prova? ")  # Usa a função para garantir limite
notateste = obter_nota("Qual sua nota do teste? ")
notaav = obter_nota("Nota de Atividade Avaliativa: ")

# Cálculo da nota
notaf = 2 * notaprova + notateste + 4 * notaav 
notafinal = notaf / 7

# Exibição do boletim
print("\nNome do aluno | NP | NT | NAV | Nota Final")
print("=========================================")
print(f"{nome} | {notaprova:.1f} | {notateste:.1f} | {notaav:.1f} | {notafinal:.2f}")
print("=========================================")
