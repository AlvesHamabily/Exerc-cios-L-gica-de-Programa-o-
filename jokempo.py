import random

def main():
    opcoes = ['pedra', 'papel', 'tesoura']
    jogador = input("Escolha pedra, papel ou tesoura: ")
    maquina = random.choice(opcoes)
    print(f"A máquina escolheu: {maquina}\n")
    
    if (jogador == maquina):
        print("Empate!")
    elif (jogador == 'pedra' and maquina == 'tesoura') or \
         (jogador == 'papel' and maquina == 'pedra') or \
         (jogador == 'tesoura' and maquina == 'papel'):
        print("Você ganhou!")
    else:
        print("Máquina ganhou!")

def reiniciar():
    while True:
        main()
        continuar = input("\nDeseja jogar novamente? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por jogar!")
            break

reiniciar()
