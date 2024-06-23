#algoritmo da tabuada
#desenvolvido por: @alveshamabily
def main():
    i = 0
    num = int(input("Informe um número natural qualquer:    "))
    while(i <= 10):  
        print('{0} X {1} = {2}'.format(i, num, (i * num)))  
        i = i + 1   
main()


