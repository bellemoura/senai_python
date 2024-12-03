  # Pedir para o usuário digitar os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

  # Calcular a média
media = (num1 + num2 + num3 + num4) / 4

  # Mostrar o resultado
print("A média dos números é:", media)

if (media<5):
    print(f'\033[31m Reprovado - Média: {media}\033[m')
elif(media>=5 and media<7):
    print(f'Aprovado com Regular - Média: {media}')
elif(media>=7 and media<9):
    print(f' Aprovado com Bom - Média: {media}')
elif(media>=9 and media<=10):
    print(f'Aprovado com Excelente - Média: {media}')
else:
          print(f'A média é maior que 10, digite valores válidos!!')