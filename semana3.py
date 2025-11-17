def dados_pessoais(nome,idade) :
	print("\n=== RESULTADO ===")
	print(f"olá, {nome}! Você tem {idade} anos.")
	if idade >= 18: 
		print("Você é maior de idade.")
	else:
		print("Você é menor de idade.")
		
print("=== VERIFICADOR DE IDADE ===")

nome= input("Digite seu nome: ")

try:
	idade = int(input("Digite sua idade: "))
	dados_pessoais(nome,idade)
except ValuError:
	print("Error: por favor,digite apenas números para a idade.")