"""

A classe Manage será utilizada para cadastrar os pedidos das lojas, encontrar e priorizar os motoboys e calcular as comissões

"""



class Manage:
    """Classe Manage."""
    def __init__(self, lista_motoboy, pedidos):
        """
        Entrada de Valores:

         lista_motoboy = Lista de todos os motoboys criado pela Classe Motoboy
         pedidos = Lista de dicionário com os pedidos das lojas
        """
        self.motoboys = lista_motoboy
        self.pedidos = pedidos

    def respostas(self):
        """
         Método resposta:

         Método principal da classe, ele chama o metodo criando_pedido que tem como objetivo acessar as instâncias das lojas e
         cadastrar os pedidos e delegar o pedido para o motoboy priorizado.

         Após o método criando_pedido finalizar. O método resposta por um loop for acessa todos os motoboys e retorna por uma lista de dicionário,
         quem é o motoboy, quantodos pedidos ele tem, de quais lojas e quanto ele tem de comissão prevista no dia.
        """
        # [self.criando_pedido(self.pedidos[x]['loja'], self.pedidos[x]['valor']) for x in range(len(self.pedidos))]

        # for x in range(len(self.pedidos)):
        #     self.criando_pedido(self.pedidos[x]['loja'], self.pedidos[x]['valor'])

        # self.respostas = dict()
        # self.lista_resposta = []
        #
        # for i in self.lista_motoboy:
        #     self.respostas['motoboy'] = i.nome
        #     self.respostas['Pedidos'] = i.quantidade_entregas_ativas()
        #     self.respostas['De qual loja é'] = i.vizualizar_loja_entrega()
        #     self.respostas['Comissão'] = self.calculando_comissão(i)
        #     self.lista_resposta.append(self.respostas.copy())
        #
        # print(self.lista_resposta)

        for p in self.pedidos:
            self.criando_pedido(p['loja'], p['valor'])

        l = []

        for m in self.motoboys:
            l.append({
                'motoboy': m.nome,
                'Pedidos': m.quantidade_entregas_ativas(),
                'De qual loja é': m.vizualizar_loja_entrega(),
                'Comissão': self.calculando_comissão(m),
            })

        return l

    def criando_pedido(self, loja, valor):
        """
        Cadastra o pedido da loja pelo método da classe Loja,
        Após cadastrar todos os pedidos das lojas o método vai chamar o método delegar_entrega
        que vai delegar os pedidos para os motoboys com menos entrega ativa.

        loja = objeto
        valor = float
        """
        loja.cadastro_pedido(valor)
        self.delegando_entrega(loja, loja.inde_ultimo_pedido())

    def delegando_entrega(self, loja, id):
        """
        O Método vai verificar primeiro se a loja que cadastrou o pedido tem algum motoboy com prioridade atraves
        do método encontrar_motoboy_prioridade, caso sejá verdadeira essa condição o método encontrar_motoboy_prioridade
        vai priorizar o(s) motoboy(s) com prioridade na loja caso contrário o Método encontra_motoboy é chamado e a
        priorização considera todos os motoboys.

        loja = objeto
        id = inteiro
        """

        if self.encontra_motoboy_prioridade(loja, id) == False:
            self.encontra_motoboy(loja, id).pegando_entrega(loja.retornar_nome(), loja.enviando_pedido(id)[0],
                                                    loja.enviando_pedido(id)[2])
        else:
            self.encontra_motoboy_prioridade(loja, id).pegando_entrega(loja.retornar_nome(),
                                                                                   loja.enviando_pedido(id)[0],
                                                                                   loja.enviando_pedido(id)[2])

    def encontra_motoboy_prioridade(self, loja, id):
        """
        O Método procura se tem algum motoboy com prioridade para a loja e cria uma lista com os motoboys com prioridade,
        com essa lista criada, o Método ordena todos os motoboys encontrados em uma lista do que tem menos entregas ativas
        para o que tem mais entregas ativas. Com essa lista criada o método verifica o valor da comissão que vai ser paga para
        o motoby casa o valor da comissão seja menor do que a média de todas as possíveis comissões ou a comissão seja menor que
        a do segundo motoboy a função prioriza o primeiro motoboy. Se as duas condições forem falsas e o primeiro motoboy
        tiver menos corrida que a média de corridas ativas para todos os motoboy, o método continua priorizando o primeiro motoboy.
        Caso contrário o segundo motoboy vai ser priorizado


        loja = objeto
        id = inteiro
        """

        lista_encontra_motoboy_prioridade = [m for m in self.motoboys
                                             if loja.retornar_nome() in m.vizualizar_prioridade()]

        if len(lista_encontra_motoboy_prioridade) == 0:
            return False

        else:
            a = sorted([[lista_encontra_motoboy_prioridade[i],(loja.enviando_pedido(id)[0]*loja.enviando_pedido(id)[2])+ lista_encontra_motoboy_prioridade[0].taxa,
                            lista_encontra_motoboy_prioridade[i].quantidade_entregas_ativas()] for i in
                           range(len(lista_encontra_motoboy_prioridade))], key=lambda x: x[-1])



            if len(lista_encontra_motoboy_prioridade) <= 1:
                b = a[0][0]

            elif a[0][1] <= sum([x[1] for x in a]) / len(self.lista_encontra_motoboy_prioridade):
                b = a[0][0]

            elif a[0][1] <= a[1][1]:
                b = a[0][0]

            elif a[0][1] > a[1][1] and a[0][2] < sum([x[2] for x in a]) / len(self.lista_encontra_motoboy_prioridade):
                b = a[0][0]

            else:
                b = a[1][0]

            return b

    def encontra_motoboy(self,loja, id):
        """
        O Método ordena todos os motoboys cadastrados em uma lista do que tem menos entregas ativas
        para o que tem mais entregas ativas. Com essa lista criada o método verifica o valor da comissão que vai ser paga para
        o motoby casa o valor da comissão seja menor do que a média de todas as possíveis comissões ou a comissão seja menor que
        a do segundo motoboy a função prioriza o primeiro motoboy. Se as duas condições forem falsas e o primeiro motoboy
        tiver menos corrida que a média de corridas ativas para todos os motoboy, o método continua priorizando o primeiro motoboy.
        Caso contrário o segundo motoboy vai ser priorizado

        loja = objeto
        id = inteiro
        """

        a = sorted([[self.motoboys[i], (loja.enviando_pedido(id)[0] * loja.enviando_pedido(id)[2]) + self.motoboys[i].taxa,
                     self.motoboys[i].quantidade_entregas_ativas()] for i in
                    range(len(self.motoboys))], key=lambda x: x[-1])


        if a[0][1] <= sum([x[1] for x in a]) / len(self.motoboys):
            b = a[0][0]

        elif a[0][1] <= a[1][1]:
            b = a[0][0]

        elif a[0][1] > a[1][1] and a[0][2] < sum([x[2] for x in a]) / len(self.motoboys):
            b = a[0][0]

        else:
            b = a[1][0]

        return b

    def calculando_comissão(self, Motoboy):
        """
        Método calcula a comissão total do motoboy do dia somando todas as comissões cadastrada para o motoboy acessando pelo metodo
        lista_entregas_ativas da classe Motoboy.

        Motoboy: instância de um motoboy da classe Motoboy
        """
        return sum(Motoboy.lista_entregas_ativas()[i]['comissao'] for i in range(len(Motoboy.lista_entregas_ativas())))