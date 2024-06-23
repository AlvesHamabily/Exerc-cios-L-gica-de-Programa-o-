#algoritmo para calcular horas trabalhadas de um operário
#desenvolvido por @alveshamabily
def Salario(cod, nHoras):
    if(nHoras<=50):
        salario = float(nHoras*10)
        print(f'A remuneraçaõ de {cod} é R${salario}')
    elif(nHoras>50):
        hr_e = nHoras-50
        e = hr_e*20
        salario = 50*10
        print(f'A remuneraçaõ de {cod} é \nSalário base: R${salario}')
        print(f'Salário excedente: R${e}')
    else:
        print('Dados inválidos. Tente novamente com valores aceitos.')
        

def main():
    cont = 1
    while cont==1:
        c = input('Código pessoal do operário:  ')
        n = float(input('Horas trabalhadas: '))
        
        print(Salario(c, n))
        cont=int(input('Deseja calcular o salário de outro operário? (1) para Sim ou pressione 0 para sair   '))
        if (cont==0):
            break

main()