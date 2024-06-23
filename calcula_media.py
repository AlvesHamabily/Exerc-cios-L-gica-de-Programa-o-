
#Algoritmo para calcular media do aluno com 5 notas 
#desenvolvido por @alveshaabily

def Media(name, lista):
    med = float(sum(lista)/5)
    print("")
    print(f"Média: {med}")
    if(med<=5):
        print(f"{name}, sua nota não foi suficiente para aprovação.  Estado: não aprovado!")
    elif(med>=5 and med<=7):
        print(f"{name}, sua nota foi não foi suficiente para aprovação.  Estado: recuperação!")
    elif(med>7):
        print(f"{name}, sua nota é suficiente. Média: Estado:  aprovado!")

def main():

    nome = input("Seja Bem vindo(a). Informe seu nome: ")
    list = []
    n1 = int(input("Informe a primera nota a ser calculada: "))
    list.append(n1)
    n2 = int(input("Informe a segunda nota a ser calculada: "))
    list.append(n2)
    n3 = int(input("Informe a terceira nota a ser calculada: "))
    list.append(n3)
    n4 = int(input("Informe a quarta nota a ser calculada: "))
    list.append(n4)
    n5 = int(input("Informe a quinta nota a ser calculada: "))
    list.append(n5)
    Media(nome, list)

main()