# Calculadora com loop e match-case

while True:
    print("\n=== CALCULADORA DA REBECCA ===")
    print("Operações disponíveis: +  -  *  /")
    print("Digite 'sair' para encerrar o programa.\n")

    # Entrada do usuário
    operacao = input("Escolha a operação (+, -, *, / ou 'sair'): ")

    # Verifica se o usuário quer encerrar
    if operacao.lower() == "sair":
        print("Encerrando a calculadora...obrigado por utilizar.. Até mais!")
        break

    # Pede os números apenas se a operação for válida
    if operacao in ['+', '-', '*', '/']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Estrutura match-case (Python 3.10+)
            match operacao:
                case '+':
                    resultado = num1 + num2
                    print(f"Resultado: {num1} + {num2} = {resultado}")
                case '-':
                    resultado = num1 - num2
                    print(f"Resultado: {num1} - {num2} = {resultado}")
                case '*':
                    resultado = num1 * num2
                    print(f"Resultado: {num1} * {num2} = {resultado}")
                case '/':
                    if num2 != 0:
                        resultado = num1 / num2
						print(f"Resutado : {num1} / {num2} = {resultado}")
					else:
						print("Erro : divisão por zero não é permitida.")
		except VslueError:
			print("Erro: digite apenas números válidos!")
	else:
		print("Operação inválida! Tente novamente.")