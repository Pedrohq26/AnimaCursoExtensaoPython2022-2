#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é bichão, mesmo..."
nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota: "))

if (nota == 10):
  print(f"{nome}, voce passou do ano e foi incrivel")
  
elif (nota >=6 and nota < 10):
  print(f"{nome} Voce passou na média")

else: # é sempre automaticamente o que as duas condições não tratou
  print("Voce não passou de ano")
  