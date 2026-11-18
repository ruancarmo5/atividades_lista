#Exercício 4
menor_numero = 9999999
maior_numero = 0
Lista = []

while True:
  opcao = int(input("Digite 1 para continuar e 2 para parar: "))
  if opcao == 1:
    numero = int(input("Insira um número: "))
    Lista.append(numero)

    if numero > maior_numero:
      maior_numero = numero  

    if numero < menor_numero:
      menor_numero = numero  
  else:
    break  

media = (maior_numero * menor_numero) ** (1 / 2)
print(Lista)
print(f"A média geométrica entre o maior número e o menor número é de {media}")