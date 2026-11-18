#Exercício 3
strings = []
palavra = ''
caracteres = 0
for i in range(5):
    p = input("Digite uma palavra: ")
    strings.append(p)
    c=len(p)
    if c > caracteres:
        caracteres = c
        palavra = p
print(f'A maior palavra é {p} com {c} caracteres.')
