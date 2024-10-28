produto = float(input("Digite o valor de um produto: R$"));

if(produto > 100):
    desconto = produto - (0.10 * produto);

print(f"Valor com desconto R$ {desconto}");