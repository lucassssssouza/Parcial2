#Pede o primeiro numero, se a conta irá ser de mais, menos, vezes e divisão e por fim o segundo numero
num1 = float(input("Primeiro número: "))
op = input("Operação (+, -, *, /): ")
num2 = float(input("Segundo número: "))
#Abaixo faz os calculos de acordo com a operação que você colocou acima
if op == "+":
    print("Resultado:", num1 + num2)
elif op == "-":
    print("Resultado:", num1 - num2)
elif op == "*":
    print("Resultado:", num1 * num2)
elif op == "/":
    print("Resultado:", num1 / num2)
else:
    print("Resultado inválido")
      #Se o resultado der algo como uma operação errada ou digitação errada (algo que não esteja no codigo) irá aparecer "Resultado Invalido"
