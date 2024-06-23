#algoritmo para calcular pagamento de comissão por vendas
#desenvolvido por: @alveshamabily

class Vendedor:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Peca(Vendedor):
    def __init__(self, name, id, cod, valor, quantidade):
        super().__init__(name, id)
        self.cod = cod
        self.valor = valor
        self.quantidade = quantidade

    def Venda(self):
        venda = self.valor * self.quantidade
        return venda
    
    def Comissao(self, venda):
        cms = venda * 0.5
        return cms

def main():
    nome = input("Informe o nome do vendedor: ")
    id = input("Informe seu código de identificação: ")
    codigo = int(input("Informe o código da peca: "))
    preco = float(input("Valor unitário: R$"))
    qtd_vendida = int(input("Quantidade de peças vendidas: "))
    v1 = Vendedor(nome, id)
    p1 = Peca(nome, id, codigo, preco, qtd_vendida)

    total_venda = p1.Venda()
    comissao = p1.Comissao(total_venda)

    print(f"Total de vendas: R${total_venda:.2f}")
    print(f"Comissão do vendedor {v1.get_name()}: R${comissao:.2f}")

main()