#Exercício 5
import random
rifa = []
while True:
    opcao = int(input("Insira 1 para adicionar um participante e 2 para sair: "))
    if opcao == 1:
        participante = input("Insira o nome do participante: ")
        rifa.append(participante)
    else:
        break
sorteado = random.choice(rifa)
print(f'O ganhador da rifa foi {sorteado}')