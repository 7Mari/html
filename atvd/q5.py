idade = int(input("Digite sua idade: "));

if(idade < 16):
    print("Não é obrigatório votar");
elif(idade >= 16 and idade < 18):
    print("É opcional votar");
else:
    print("É obrigatório votar");


