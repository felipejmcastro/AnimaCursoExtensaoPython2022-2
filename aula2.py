nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
dobro = idade * 2

print ("Oi {} voce tem {} anos".format(nome,idade))
print("O dobro da idade informada é {}".format(dobro))

if (idade >= 18):
  print("Voce é maior de idade, já pode dirigir")
else:
  print("Voce ainda nao pode dirigir")

genero = input("Informe o genero M = masculino, F = feminino, 0 = outros:")

if (idade >= 18 and genero == "M"):
  print("...voce tambem precisa/precisou prestar o servico militar")


  






