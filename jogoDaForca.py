import random
palavras = ["gato","cachorro","pato","elefante","leao"]
palavra_secreta = random.choice(palavras)
letras_certas = []
letras_erradas = []
vidas = 5

print("Bem vindo ao jogo da forca sobre animais")
print(f"A palavra secreta possui: {len(palavra_secreta)} letras")

while vidas > 0:
    acertou = True
    for letra in palavra_secreta:
        if letra in letras_certas:
            print(letra, end=" ")
        else:
            print("_",end=" ")
            acertou= False
    if acertou:
        print("\n Parabens você ganhou!")
        break
    print(f"Tentativas restantes {vidas}")
    letra_tentativa=input("Digite uma letra: ")

    if letra_tentativa in letras_certas or letra_tentativa in letras_erradas:
        print("Você já tentou essa letra. Tente de novo")
    elif letra_tentativa in palavra_secreta:
        letras_certas.append(letra_tentativa)
    else:
        letras_erradas.append(letra_tentativa)
        vidas-=1
        print(f"A letra: {letra_tentativa} não faz parte da palavra secreta")

    if vidas==0:
        print("Você  perdeu tente novamente")
        print(f"A palavra secreta era {palavra_secreta}")