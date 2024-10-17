peso = float(input(f"Digite o peso dos peixes: "));
multa = 4;


if(peso > 50):
    excesso = peso - 50;
    print(f"Peso Excedido: {excesso} kg");

total = excesso * multa;    


print(f"Valor da multa: R${total}");

