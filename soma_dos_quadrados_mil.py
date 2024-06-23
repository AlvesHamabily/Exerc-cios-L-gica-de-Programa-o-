#Algoritmo apra somar o quadrado de 4 numeros e fazer uma verificação caso o quadrado do terceiro seja >=1000
#Desenvolvido por @alveshamabily

def soma(n1, n2, n3, n4):
    num1=n1**2
    num2=n2**2
    num3=n3**2
    num4=n4**2

    if (num3>=1000):
        print(f"O quadrado de {n3} é = {num3}")
    else:
        print(f'''
{n1}² = {num1} \n{n2}² = {num2} \n{n3}² = {num3}\n{n4}² = {num4}
              ''')
  
def main():
    print("Digite a seguir 4 números do tipo inteiro.")
    num1 = int(input(" "))
    num2 = int(input(" "))
    num3 = int(input(" "))
    num4 = int(input(" "))
    soma(num1, num2, num3, num4)

main()
        