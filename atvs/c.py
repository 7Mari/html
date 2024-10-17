numINT1 = int (input(f"Digite o 1º número inteiro: "));
numINT2 = int (input(f"Digite o 2º número inteiro: "));
num = float (input(f"Digite o 3º número real: "));

A = (numINT1*2) * (numINT2/2);
B = (numINT1 * 3) + num;
C = num**3;

print(f"[A]O produto do dobro do primeiro com metade do segundo: {A}");
print(f"[B]A soma do triplo do primeiro com o terceiro: {B}");
print(f"[C]Terceiro número eleveado ao cubo: {C}");