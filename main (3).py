# comando input(): quero permitir que
# o usuario digite algo. . .
nome = input("Digite seu nome: ") 
# pede a idade para o usuario
idade = int(input("Qual a sua idade? "))

#comando de saída..exibir na tela
print(f"Boa noite, seu nome é {nome}")

#exiba "sua idade é . . ."
print(f"Minha idade é {idade} anos")

# e seu eu quiser o dobro da idade informada
dobro = idade * 2
print(f"O dobro da idade informada é {dobro}")

#Estrutura condicional - o famoso "SE"(if)
#Se a pessoa  for maior de idade, mostre "Voce é maior de idade, ótimo! ja pode beber ou dirigir"
if idade >= 18: 
  print("Voce é maior de idade, ótimo! ja pode beber ou dirigir")

else:
  print("Voce é jovem ainda, não pode beber nem dirigir")

#E se eu quisessem pergurtar o genero (M = Masculino e F= Feminino)
#Mostre (...e voce tambem precisa/precisou prestar o serviço militar obrigatório)

genero = input("Informe o genero M=Masculino, F=Feminino, O=Outros: ")

if (idade >=18 and genero == "M"):
  print("Voce precisa se alistar")
  
else:
  print("Voce não precisa se alistar")
 


