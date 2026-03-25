# Aqui digita os nomes 
n1 = input("Digite o 1º nome: ")
n2 = input("Digite o 2º nome: ")
n3 = input("Digite o 3º nome: ")
n4 = input("Digite o 4º nome: ")
n5 = input("Digite o 5º nome: ")
#Aqui irá ter a lista dos nomes pela ordem que antes você digitou
nomes = [n1, n2, n3, n4, n5]
print("\nLista de Nomes:")
for nome in nomes:
    print(f"- {nome}")
