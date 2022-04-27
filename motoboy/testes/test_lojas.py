from SistemaEntrega import Loja


def test_init():
    loja = Loja('Loja1', 0.05)

    assert loja.comi == 0.05
    assert loja.nome == 'Loja1'

def test_trocar_comissao():
    loja = Loja('Loja1', 0.05)
    loja.trocar_comissao(0.15)

    assert loja.comi == 0.15

def test_cadastro_pedido():
    loja = Loja('Loja1', 0.05)
    loja.cadastro_pedido(50)

    assert len(loja.lista_pedido) == 1
    assert loja.lista_pedido[0]['PEDIDO'] == 'PEDIDO 1'
    assert loja.lista_pedido[0]['Valor'] == 50
    assert loja.lista_pedido[0]['Loja'] == 'Loja1'

def test_enviando_pedido():
    loja = Loja('Loja1', 0.05)
    loja.cadastro_pedido(50)
    pedido = loja.enviando_pedido(loja.inde_ultimo_pedido())

    assert pedido[0] == 50
    assert pedido[1] == 'Loja1'
    assert pedido[2] == 0.05


