#desenvolvido por: @alveshamabily

def main():
    i = 1
    aluno = 11
    for i in range(aluno):
        print('-' *30)
        n1 = float(input(f'1° nota do {i}° aluno:   '))
        n2 = float(input(f'2° nota do {i}° aluno:   '))
        media = (n1 + n2)/2
        print(f"Média do {i}° aluno = {media}")

main()