genero = input(f"Digite seu gênero [Masculino ou Feminino]: ");
altura = float (input(f"Digite sua altura: "));

if(genero == 'M'):
    pesoIdeal = (72.7 * altura)- 58;
else:
    pesoIdeal = (62.1 * altura)- 44.7;


print(f"Peso Ideal: {pesoIdeal}");
