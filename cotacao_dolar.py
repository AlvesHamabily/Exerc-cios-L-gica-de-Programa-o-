#Algoritmo para conversão de moedas (dólar e real)
#Desenvolvido por @alveshamabily

def converte(d, r):
    val = float(d*r)
    return val
    breakpoint

def main():
    valor_dolar = float(input("Informe a cotação do dólar americano:   U$"))
    valor_real = float(input("Qual valor deseja converter?:   R$"))

    print(f"R${valor_real} em dólar = U${converte(valor_dolar, valor_real):.2f}")  

main()