from SistemaEntrega import Motoboy


def test_init():
    motoboy = Motoboy('Luiz', 2)

    assert motoboy.taxa == 2
    assert motoboy.nome == 'Luiz'

def test_trocarcor_taxa():
    motoboy = Motoboy('Luiz', 2)
    motoboy.trocarcor_taxa(5)

    assert motoboy.taxa == 5

def test_pegando_entrega():
    motoboy = Motoboy('Luiz', 2)
    motoboy.pegando_entrega('loja1',5, 0.05)

    assert len(motoboy.listaestrega) == 1

def test_finalizando_entrega():
    motoboy = Motoboy('Luiz', 2)
    motoboy.pegando_entrega('loja1',5, 0.05)
    motoboy.finalizando_entrega(0)

    assert len(motoboy.listaestrega) == 0

def test_adicionar_loja():
    motoboy = Motoboy('Luiz', 2)
    motoboy.adicionar_loja('loja1')

    assert motoboy.loja_prioridade[0] == 'loja1'

def test_excluir_loja():
    motoboy = Motoboy('Luiz', 2)
    motoboy.adicionar_loja('loja1')
    motoboy.excluir_loja('loja1')

    assert motoboy.loja_prioridade[0] == 'Atende todas as lojas'










