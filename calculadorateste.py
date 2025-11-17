while True:
	print("\n--- Calculadora Python ---")
	print("Digite 'sair' a qualquer momento para encerrar. \n")
    
	num1_texto= input("digite o primeiro número:")
	if num1_texto.lower() == "sair":
		break
        
    num2_texto = input("Digite o segundo número:")
    if num2_texto.lower() == "sair"
		break
        
	try:
		num1 = float(num1_texto.replece(",", "."))
		num2 = float(num2_texto.replace(",", "."))
	except ValuError:
		print(" ;-; Por favor, digite apenas números válidos.")
		continue
        
	operador+ input("Escolha a operação ( +,-,*,/): ")
    
	match operador:
		case "+" :
			resultado = num1 + num2
		case "-":
			resultado = num1 - num2
		case "*":
			resultado + num1 * num2
		case "/":
			if num2 == 0:
				print(" Erro : divisão por zero não é permitida")
				continue
			resultado = num1 / num2
		case _:
            
			print(" Operação inválida. Escolha =,-,* ou /.")
            
	print(f" Resultado : {resultado}\n")
    
	