import forca
import adivinhacao

print("********************************")
print("*****Escolha o seu jogo!********")
print("********************************")

print("(1) Forca \n(2) Adivinhação")

jogo = int(input("Qual jogo?"))

if jogo == 1:
    print("jogando forca")
    forca.jogar()
elif jogo == 2:
    print("jogando advinhação")
    adivinhacao.jogar()

