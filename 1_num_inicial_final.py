#Faça um algoritmo que escreva na tela os números de um 
#número inicial a um número final. Os números inicial e  final devem ser informados pelo usuário;
##desenvolvido por: @alveshamabily
def mostrar(n1, n2):
    if(n1 < n2):
        while(n1<=n2):
            print(n1)
            n1+= 1
    else:
        while(n1>=n2):
            print(n1)
            n1-= 1

def main():
    inicial  = int(input("Digite um número qualquer: "))
    final = int(input("Digite um número para final: "))
    mostrar(inicial, final)

main()