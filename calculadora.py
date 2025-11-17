num1 = float(input("Digite o primeiro número: "))
operador = input("Escolha a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if operador == '+':
	resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    if num2 == 0:
        resultado = "Erro: divisão por zero não é permitida!"
    else:
        resultado = num1 / num2
else:
    resultado = "Operador inválido!"

print("Resultado:", resultado)
