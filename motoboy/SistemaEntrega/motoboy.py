"""
Módulo que contém as classes Motoboy.

A classe Motoboy será usada para instânciar e guardar cada motoboy cadastrado

"""

class Motoboy:
    """ Classe Motoboy"""

    def __init__(self, nome, taxa, loja_prioridade='Atende todas as lojas'):
        """
        Entrada de Valores:

        nome = nome do motoboy (String)
        taxa = taxa que o motoboy cobra por entrega (float)
        loja = Loja que o motoboy tem prioridade - Valor padrão = 'Atende todas as lojas' (String)
        """
        self.nome = nome
        self.taxa = taxa
        self.loja_prioridade = [loja_prioridade]
        self.lojaentrega =[]
        self.entrega = {}
        self.listaestrega = []
        self.qtdentregas_realizadas = 0

    def detalhar(self):
        """ Detalha as informações do motoboy"""
        print(f"Nome do Motoboy: {self.nome}")
        print(f"A taxa de entrega do Motoboy é: {self.taxa}")
        print(f"O motoboy tem prioridade na loja:{self.loja}")
        print(f"O motoboy tem: {len(self.listaestrega)}, entregas ativas e um total de {self.qtdentregas_realizadas} entregas, realizadas")

    def quantidade_entregas_ativas(self):
        """ Retorna a quantidade de entregas ativas"""
        return len(self.listaestrega)

    def vizualizar_loja_entrega(self):
        """ Retorna os lojas com entrega ativa"""
        return self.lojaentrega

    def nome_motoboy(self):
        """ Retorna o nome do motoboy"""
        return self.nome()

    def taxa_motoboy(self):
        """ Retorna a taxa do motoboy"""
        return int(self.taxa)

    def lista_entregas_ativas(self):
        """Retorna a lista de entregas"""
        return self.listaestrega

    def vizualizar_prioridade(self):
        """Retorna as lojas de prioridade do motoboy"""
        return self.loja_prioridade

    def trocarcor_taxa(self, taxa):
        """
        Atualiza a taxa de cobrança do motoboy
        taxa = float
        """
        self.taxa = taxa
        print(f'Valor da taxa atualizado para: {self.taxa}')

    def adicionar_loja(self, loja_prioridade):
        """
        Adiciona loja de prioridade do Motoboy
        loja_prioridade = string
        """
        if self.loja_prioridade[0] == 'Atende todas as lojas':
            self.loja_prioridade.remove('Atende todas as lojas')
            self.loja_prioridade.append(loja_prioridade)
        elif loja_prioridade in self.loja_prioridade:
            print('Essa loja já está cadastrada')
        else:
            self.loja.append(loja_prioridade)

    def excluir_loja(self, loja_prioridade):
        """
        Exclui loja de prioridade do motoboy
        loja_prioridade = string
        """
        if loja_prioridade not in self.loja_prioridade:
            print('Essa loja não está cadastrada')
        else:
            self.loja_prioridade.remove(loja_prioridade)

        if len(self.loja_prioridade) == 0:
            self.loja_prioridade.append('Atende todas as lojas')

    def pegando_entrega(self, loja, valor, comi):

        self.entrega['loja'] = loja
        self.entrega['valor'] = valor
        self.entrega['comissao'] = (valor * comi) + self.taxa
        self.listaestrega.append(self.entrega.copy())
        self.lojaentrega.append(loja)
        print(f'{self.nome}, pegou a sua entrega! Ele tem {len(self.listaestrega)} entregas, ativas')

    def verificar_entregas_ativas(self):
        """ O Motoboy verifica as entregas ativas """
        if len(self.listaestrega) == 0:
            print("Você não tem entregas ativas")
        else:
            print([{'id': x, 'entrega': y} for x, y in enumerate(self.listaestrega)])

    def finalizando_entrega(self, id):
        """
        O Motoboy finaliza as entregas realizadas
        id = inteiro
        """
        try:
            del self.listaestrega[id]
            self.qtdentregas_realizadas += 1
            print('Entrega finalizada com sucesso')

        except:
            print('Valor da entrega não ativo')
            print('Você tem as entregas abaixo ativa')
            print([{'id': x, 'entrega': y} for x, y in enumerate(self.listaestrega)])