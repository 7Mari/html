idade = int(input("Digite sua idade: "));

if(idade < 18):
    print("Menor de Idade");
elif(idade >= 18 and idade < 60):
    print("Adulto");
else:
    print("Idoso");

