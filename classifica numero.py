#Algoritmo para classificar um número dado pelo usuário
#Desenvolvido por @alveshamabily

def par(n):
    if(n % 2 == 0):
        print(f'{n} é par')
    else:
        print(f'{n} é ímpar')

def positivo(n):
    if(n>=0):
        print(f'{n} é positivo')
    else:
        print(f'{n} é negativo')

def main():
    num = float(input('Informe um númeor qualquer:  '))
    par(num)
    positivo(num)

main()