
"""

A classe Loja será usada para instânciar e guardar cada loja cadastrada

"""




class Loja:
    """ Classe Loja"""
    def __init__(self, nome, comi):
        """
        Entrada de Valores:

        nome = nome da loja (String)
        comi = comissão que a loja paga por entrega (float)
        """
        self.nome = nome
        self.comi = comi
        self.pedido = dict()
        self.lista_pedido = []
        self.qtdpedido = 0

    def inde_ultimo_pedido(self):
        """Retorna o ID do ultimo pedido para apoira nos metodos da classe Manage"""
        return len(self.lista_pedido) - 1

    def detalhar(self):
        """ Detalha as informações da loja"""
        print(f"A comissão da loja {self.nome} é: {self.comi * 100} %")

    def retornar_nome(self):
        """ Retona o nome da loja """
        return self.nome

    def trocar_comissao(self, comi):
        """ Troca a comissão que a loja paga por entrega """
        self.comi = comi

    def cadastro_pedido(self, valor):
        """
        Cadastra os pedidos da loja
        Valor = float
        """
        self.qtdpedido += 1
        self.pedido['PEDIDO'] = f'PEDIDO {self.qtdpedido}'
        self.pedido['Valor'] = valor
        self.pedido['Loja'] = self.nome
        self.lista_pedido.append(self.pedido.copy())
        print(f'{self.nome}, pedido cadastrado com sucesso! Você tem {len(self.lista_pedido)} pedidos!')

    def enviando_pedido(self, id):
        """
        Cria uma lista com [Valor, Loja, Comissão] para todos os pedidos ativos da loja
        """
        ep = [{'id': x, 'pedido': y} for x, y in enumerate(self.lista_pedido)]
        return [ep[id]['pedido']['Valor'], ep[id]['pedido']['Loja'], self.comi]

    def verificar_pedidos_ativos(self):
        """ Informa todos os pedidos ativos da loja"""
        if len(self.lista_pedido) == 0:
            print("Você não tem pedidos ativas")
        else:
            print([{'id': x, 'pedido': y} for x, y in enumerate(self.lista_pedido)])