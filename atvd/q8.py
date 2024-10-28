salario = float(input("Digite o valor de seu salário: R$"));

if(salario < 1000):
    aumento = (0.10 * salario) + salario;
else:
    aumento = (0.05 * salario) + salario;

print(f"R$ {aumento}");
