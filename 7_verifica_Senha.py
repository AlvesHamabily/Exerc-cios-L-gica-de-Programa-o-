#desenvolvido por: @alveshamabily
def verifica_senha(lista):
    comp = input("Informe sua senha:    ")
    if(comp == lista[1]):
        print(f"Bem vindo(a), {lista[0]}.")
    else:
        print("Sena incorreta! Por favor verifique seus dados novamente.")


def main():
    
    p = []
    nome = input("Bem vindo. Infome seu nome para conrinuar:    ")
    p.append(nome)
    senha = input("\nCadastre a sua senh. Por favor utilize uma senha forte...  ")
    p.append(senha)
    print(f'{nome}, Senha salva com Sucesso!')

    acao = int(input("Deseja verificar sua senha (1) ou sair? (2)"))
    if acao ==1:
        verifica_senha(p)
    else:
        print("Processo encerrado! ")
    

main()
