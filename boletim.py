def obter_nota(mensagem):
    while true:
        try:
            nota - float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: A nota deve estar entre 0 e 10> Tente Novamente!")
        except ValueError:
            print("ERRO: Insira um valor válido")

# Dados
nome = input("Nome do aluno: ")
notaprova = float(input("Qual sua nota da prova? "))
notateste = float(input("Qual sua nota do teste?"))
notaav = float(input("Nota de Atividade Avaliativa"))

#cálculo da nota
notaf = 2 * notaprova + notateste +  4 * notaav 
notafinal = notaf / 7

#exibição do boletim
print("Nome do aluno","|", "NP","|", "NT","|", "NAV","|", "Nota Final")
print("================================================")
print(f"{nome} | {notaprova:.1f} | {notateste:.1f} | {notaav:.1f} | {notafinal:.2f}")
print("================================================")
