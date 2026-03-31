#Coloca-se os dados necessarios para o calculo
C = float(input("Digite o Capital (C): "))
I = float(input("Digite a Taxa de juros em % (I): "))
T = float(input("Digite o Tempo (T): "))


# Aqui ocorre a fórmula: J = (C * I * T) / 100
J = (C * I * T) / 100

# Exibe o resultado com duas casas decimais
print(f"\nCom um capital de R$ {C:.2f}, taxa de {I}% e tempo de {T},")
print(f"o valor dos juros (J) é: R$ {J:.2f}")
