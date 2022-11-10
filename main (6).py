contador = 1
#print(contador)
#contador = contador+1 #contador += 1
#print(contador)
#contador += 1
#print(contador)

while(contador <=10):
  print(contador)
  contador = contador+1

# Laço(while) for (python for = for each)
fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pera"

# Lista
frutas = ["morango", "laranja", "pera"] 
# Mostras todas
print(frutas)
# Quero exibir apenas a terceira fruta(pera)
# A lista começa contando do 0
print(frutas[0])
print(frutas[2])

# Exibir quantas frutas tem na minha lista?
print(len(frutas)) #length = tamanho 

# Quero incluir uma fruta nova
frutas.append("manga")

print(len(frutas)) #length = tamanho 
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

print("Exemplo das frutas com while")
frutas.append("uva")

i=0 #(i de index)
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das frutas com FOR")
for frutas in frutas:
  print(frutas)

