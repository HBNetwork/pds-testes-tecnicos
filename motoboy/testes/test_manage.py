from SistemaEntrega import Manage, Loja, Motoboy



def test_init():
    # Criando os Motoboys

    Moto_1 = Motoboy('Luiz', 2, 'Loja1')
    Moto_2 = Motoboy('Arthur', 3)

    lista_motoboy = [Moto_1, Moto_2]

    # Criando as Lojas

    Loja_1 = Loja('Loja1', 0.05)
    Loja_2 = Loja('Loja2', 0.05)

    # Pedidos

    pedidos = [{'loja': Loja_1, 'valor': 50, 'pedido': 'PEDIDO1'},
               {'loja': Loja_1, 'valor': 50, 'pedido': 'PEDIDO2'},
               {'loja': Loja_2, 'valor': 50, 'pedido': 'PEDIDO1'}]

    manage = Manage(lista_motoboy, pedidos)

    assert len(manage.motoboys) == 2
    assert len(manage.pedidos) == 3

def test_criando_pedido():
    # Criando os Motoboys

    Moto_1 = Motoboy('Luiz', 2, 'Loja1')
    Moto_2 = Motoboy('Arthur', 3)

    lista_motoboy = [Moto_1]

    # Criando as Lojas

    Loja_1 = Loja('Loja1', 0.05)
    Loja_2 = Loja('Loja2', 0.05)

    # Pedidos

    pedidos = [{'loja': Loja_1, 'valor': 50, 'pedido': 'PEDIDO1'},
               {'loja': Loja_1, 'valor': 50, 'pedido': 'PEDIDO2'},
               {'loja': Loja_2, 'valor': 50, 'pedido': 'PEDIDO1'}]


    manage = Manage(lista_motoboy, pedidos)
    manage.criando_pedido(pedidos[0]['loja'], pedidos[0]['valor'])

    assert len(Loja_1.lista_pedido) == 1
    assert Loja_1.lista_pedido[0]['PEDIDO'] == 'PEDIDO 1'
    assert Loja_1.lista_pedido[0]['Valor'] == 50
    assert Loja_1.lista_pedido[0]['Loja'] == 'Loja1'


def test_encontra_motoboy_prioridade():
    # Criando os Motoboys

    Moto_1 = Motoboy('Luiz', 2, 'Loja1')
    Moto_2 = Motoboy('Arthur', 1)

    lista_motoboy = [Moto_1, Moto_2]

    # Criando as Lojas

    Loja_1 = Loja('Loja1', 0.05)
    Loja_2 = Loja('Loja2', 0.05)

    # Pedidos

    pedidos = [{'loja': Loja_1, 'valor': 50, 'pedido': 'PEDIDO1'},
               {'loja': Loja_1, 'valor': 50, 'pedido': 'PEDIDO2'},
               {'loja': Loja_2, 'valor': 50, 'pedido': 'PEDIDO1'}]


    manage = Manage(lista_motoboy, pedidos)
    manage.criando_pedido(pedidos[0]['loja'], pedidos[0]['valor'])
    motoboy = manage.encontra_motoboy_prioridade(pedidos[0]['loja'], pedidos[0]['loja'].inde_ultimo_pedido())
    assert motoboy == Moto_1

def test_encontra_motoboy():
    # Criando os Motoboys

    Moto_1 = Motoboy('Luiz', 100, 'Loja1')
    Moto_2 = Motoboy('Arthur', 1)

    lista_motoboy = [Moto_1, Moto_2]

    # Criando as Lojas

    Loja_1 = Loja('Loja1', 0.05)
    Loja_2 = Loja('Loja2', 0.05)

    # Pedidos

    pedidos = [{'loja': Loja_1, 'valor': 50, 'pedido': 'PEDIDO1'},
               {'loja': Loja_1, 'valor': 50, 'pedido': 'PEDIDO2'},
               {'loja': Loja_2, 'valor': 50, 'pedido': 'PEDIDO1'}]



    manage = Manage(lista_motoboy, pedidos)
    manage.criando_pedido(pedidos[2]['loja'], pedidos[2]['valor'])

    motoboy = manage.encontra_motoboy(pedidos[2]['loja'], pedidos[2]['loja'].inde_ultimo_pedido())
    assert motoboy == Moto_1