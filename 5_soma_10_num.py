#desenvolvido por: @alveshamabily
def soma(lista):
    return sum(lista)

def main():
    li = []
    i =1
    for i in range(10):
        n = int(input('Digite um número:   '))
        li.append(n)
    
    print(f"A soma de todos os números informados é = {soma(li)}")

main()