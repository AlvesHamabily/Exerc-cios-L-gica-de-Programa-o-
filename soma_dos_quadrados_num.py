#Soma dos quadrados de 4 numeros 
#Desenvolvido por @alveshamabily

def q_s(n1, n2, n3, n4):
    n1*=n1
    n2*=n2
    n3*=n3
    n4*=n4

    soma = n1+n2+n3+n4
    return soma

def main():
    print("Digite a seguir 4 números do tipo inteiro.")
    num1 = int(input(" "))
    num2 = int(input(" "))
    num3 = int(input(" "))
    num4 = int(input(" "))

    print(f"A soma dos quadrados dos números informados é: {q_s(num1, num2, num3, num4)}")

main()
        