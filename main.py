import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

comprimento_da_senha = int(input("Insira o tamanho da senha: "))

senha_gerada = ""

for i in range(comprimento_da_senha):
    letra = random.choice(caracteres)
    senha_gerada += letra

print(senha_gerada)
