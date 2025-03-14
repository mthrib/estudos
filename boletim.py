# Dados
nome = input("Nome do aluno:")
notaprova = float(input("Qual sua nota da prova? "))
notatste = float(input("Qual sua nota do teste?"))
notaav = float(input("Nota de Atividade Avaliativa"))

#cálculo
notaf = 2 * notaprova + notatste +  4 * notaav 
notafinal = notaf / 7

#tabela
print("Nome do aluno","/", "NP","/", "NT","/", "NAV","/", "Nota Final")
print("================================================")
print( nome,  notaprova,"/",     notatste,"/",   notaav, "/", notafinal)
print("================================================")
