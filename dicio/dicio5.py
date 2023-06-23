dicionario = []

while True:
    notas = int(input("Digite uma nota: "))
    dicionario.append(notas)

    resposta = input("Deseja inserir outra nota? (S/N): ")
    if resposta.upper() != "S":
        break

media = sum(dicionario) / len(dicionario)
print(f"A média das notas é: {media}")