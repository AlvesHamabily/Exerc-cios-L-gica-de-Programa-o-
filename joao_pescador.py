#Algoritmo controlador de peso e calculo de multa
#Desenvolvido por @alveshamabily

def main():
    cont = 1
    while cont == 1:
        peso = float(input("Quantidade em kg da carga: (Ex.: 20.0) "))
        excesso = 0
        multa = 0

        if(peso>50):
            excesso += float( peso - 50)
            multa += excesso*4
            print(f'''Peso da carga atual: {peso:.2f}kg
                Excesso total de Peso: {excesso:.2f}kg
                Valo de Multa: R${multa:.2f}.
            ''')
        elif(peso<50):
            print(f'''Peso da carga atual: {peso:.2f}kg
                Excesso total de Peso: {excesso:.2f}kg
                Valo de Multa: R${multa:.2f}.
            ''')

        cont = int(input("Deseja continuar ? Digite 1 para sim e para não. "))

        if cont!= 1:
            break

main()