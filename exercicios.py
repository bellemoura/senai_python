# 1. Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.
numero = int(input("Digite um número inteiro: "))
quadrado = pow (numero, 2)
print(f"O resultado de {numero}² é {quadrado}.\n\n")

# 2. Escreva um programa que leia dois caracteres e imprima-os na tela da seguinte forma:
# "O usuário digitou {caractere1} e {caractere2}!".
i = 1
num_leituras = 2 + i

while i < num_leituras:
    car = str(input(f"Digite o {i}º caractere: "))

    if i == 1:
        car1 = car
    else:
        car2 = car

    i = i + 1

print(f"O usuário digitou {car1} e {car2}!\n\n")


# 3. Crie um programa que leia um número inteiro e imprimir seu sucessor e antecessor.
numero = int(input(f"Digite um número inteiro: "))
antecessor = numero - 1
sucessor = numero + 1
print(f"O antecessor de {numero} é {antecessor}.\nO sucessor de {numero} é {sucessor}.\n\n")


# 4. Crie um programa para entrar com a base a altura de um retângulo e imprimir respectivamente 
# o perímetro e a área correspondente.
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = base * altura
perimetro = base + base + altura + altura

print(f"O perimetro é {perimetro} e a área é {area}.\n\n")


# Atividade código da aula
texto = "oi"
texto2 = str("oi")
numero = 3
numero2 = int(3)
numero3 = 3.0
numero4 = float(3)

print(texto)
print(texto2)
print(numero)
print(numero2)
print(numero3)
print(numero4)

val_feijão = float(input("\n\nQual é o valor do quilo do feijão? "))
qtd_feijão = int(input("Quantos pacotes de feijão? "))
tot_feijão = val_feijão*qtd_feijão
print(f"O valor total dos feijões é de R$ {tot_feijão}.\n\n")