-print("Qual sua nota da prova? ")
notaprova = float(input())
print("Qual sua nota do teste?")
notatste = float(input())
print("Nota de Atividade Avaliativa")
notaav = float(input())

notafinal = 2 * notaprova + notatste +  4 * notaav

print("Sua média é", notafinal / 7)
