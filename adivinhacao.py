import random

def jogar():

    print("********************************")
    print("Bem vindo no jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Informe o nivel: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu numero entre 1 e 100: ")

        print("Você digitou ", chute_str)

        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Erro: Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o numero secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor que o numero secreto.")
        rodada += 1;

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("fim do jogo")

if __name__ == "__main__":
    jogar()