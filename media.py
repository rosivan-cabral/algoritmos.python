n1 = float(input("Digite a primeira Nota: "))
n2 = float(input("Digite a segunda Nota: "))
n3 = float(input("Digite a terceira Nota:"))

media = (n1 + n2 + n3) / 3
print(f"A média do aluno é: {media}")

if media >= 7:
    print("Aprovado!")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado!")