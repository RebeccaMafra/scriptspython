while True:
    print("\n--- Calculadora Python ---")
    print("Digite 'sair' a qualquer momento para encerrar.\n")

    num1_texto = input("Digite o primeiro número: ")
    if num1_texto.lower() == "sair":
        break
    num2_texto = input("Digite o segundo número: ")
    if num2_texto.lower() == "sair":
        break

    num1_texto = num1_texto.replace(",", ".")
    num2_texto = num2_texto.replace(",", ".")

    try:
        num1 = float(num1_texto)
        num2 = float(num2_texto)
    except ValueError:
        print("❌ Por favor, digite apenas números válidos.")
        continue

    operador = input("Escolha a operação (+, -, *, /): ")

    match operador:
        case '+':
            resultado = num1 + num2
        case '-':
            resultado = num1 - num2
        case '*':
            resultado = num1 * num2
        case '/':
            if num2 == 0:
                resultado = "Erro: divisão por zero não é permitida!"
            else:
                resultado = num1 / num2
        case _:
            resultado = "Operador inválido!"

    print("Resultado:", resultado)
