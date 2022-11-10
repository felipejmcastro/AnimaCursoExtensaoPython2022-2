#criacao de funcoes

preco = 1999.90

#Calcular 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma funcao calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu...
# Isso é a declaracao da funcao(como ela funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto
  
#Aqui é o uso...
preco = 200
imposto = calcular_imposto(preco)
print(imposto)

#agora calcular imposto a alíquota agora é 7%

valores = [1.99,24.50,78.27,1515.5]
#se eu quiser calcular o imposto destes quatro valores... e exibir na tela assim: "o imposto de ... é ...."
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

#Declarar uma funcao calcular_imposto_aliquota que recebe dois parametros: o preco do produto e a aliquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota nao for informada utilize 7% como padrao.
def calcular_imposto_aliquota(valor, aliquota = 7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores: 
  print(f"O imposto do {valor} é {calcular_imposto_aliquota(valor)}")
  
#E se agora o imposto for 10%?
for valor in valores: 
  print(f"O imposto do {valor} é {calcular_imposto_aliquota(valor,10)}")