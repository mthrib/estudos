# Dados
print("Nome do Aluno: ")
nome = input()
print("Qual sua nota da prova? ")
notaprova = float(input())
print("Qual sua nota do teste?")
notatste = float(input())
print("Nota de Atividade Avaliativa")
notaav = float(input())

#cálculo
notaf = 2 * notaprova + notatste +  4 * notaav 
notafinal = notaf / 7

#tabela
print("Nome do aluno","/", "NP","/", "NT","/", "NAV","/", "Nota Final")
print("================================================")
print( nome,  notaprova,"/",     notatste,"/",   notaav, "/", notafinal)
print("================================================")
