
contador = 1

while (contador <= 10):
  print(contador)
  contador = contador + 1

frutas = ["morango","laranja","uva"]
#quero exibir apenas a 3a fruta
print(frutas[2])
print(len(frutas))
frutas.append("manga")
print(len(frutas))


print("Exemplo das frutas com while..")

i=0
while(i < len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das frutas com for..")
for fruta in frutas:
  print(fruta)
  