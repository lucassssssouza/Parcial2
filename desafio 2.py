#Digitar o numero
numero = int(input("Digite um número inteiro: "))
#Calcular os numeros,se a primeira condição for verdadeira ela será executada,e o Else afirma que se o calculo não for 0 (e o resto é 1) ele é executado
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
    #Exibe que o numero é par
else:
    print(f"O número {numero} é ÍMPAR.")
    #Exibe que o numero é impar
