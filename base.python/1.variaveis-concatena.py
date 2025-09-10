#comando de ENTRADA (tipo o scanf - interagir com usuario
#INPUT sempre pega os dados como string
nome = input("Digite seu nome: ")
dataNasc = int(input("Digite o ano que você nasceu: "))
#declarou o int para receber um valor inteiro, em vez de receber padrao que é string
altura = float(input("Digite sua altura: "))

#descobrir o tipo de variavel
print(type(nome))
print(type(dataNasc))
print(type(altura))

print(nome)
print(dataNasc)
print(altura)


#concatenar
#tipo 1
print("DADOS: ")
print("--------")
print("Nome: ", nome)
print("Ano de nascimento: ", dataNasc)
print("Altura: ", altura)

#tipo 2
print("\n\nNome: ", nome, "\nAno de nascimento: ", dataNasc, "\nAltura: ", altura)

#tipo 3 - usando F - muito legal
print(f"\n\nNome : {nome}")
print(f"Ano de nascimento: {dataNasc}")
print(f"Nota do filme: {altura}\n\n")

print(f"usando 'f' eu escrevo nome: {nome} o ano de nascimento: {dataNasc}, e a altura: {altura} sem precisar de virgulas e separações a mais!")