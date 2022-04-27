from SistemaEntrega import Motoboy, Loja, Manage



#Criando os Motoboys

Moto_1 = Motoboy('moto1', 2)
Moto_2 = Motoboy('moto2', 2)
Moto_3 = Motoboy('moto3', 2)
Moto_4 = Motoboy('moto4', 2, 'Loja1')
Moto_5 = Motoboy('moto5', 3)

lista_motoboy = [Moto_1, Moto_2, Moto_3, Moto_4, Moto_5]

# Criando as Lojas

Loja_1 = Loja('Loja1', 0.05)
Loja_2 = Loja('Loja2', 0.05)
Loja_3 = Loja('Loja3', 0.15)

# Pedidos

pedidos = [{'loja': Loja_1,'valor':50,'pedido':'PEDIDO1'},{'loja': Loja_2,'valor':50,'pedido':'PEDIDO1'},
           {'loja': Loja_3,'valor':50,'pedido':'PEDIDO1'}, {'loja': Loja_1,'valor':50,'pedido':'PEDIDO2'},
           {'loja': Loja_2,'valor':50,'pedido':'PEDIDO2'}, {'loja': Loja_3,'valor':50,'pedido':'PEDIDO2'},
           {'loja': Loja_1,'valor':50,'pedido':'PEDIDO3'}, {'loja': Loja_2,'valor':50,'pedido':'PEDIDO3'},
           {'loja': Loja_3,'valor':100,'pedido':'PEDIDO3'}, {'loja': Loja_2,'valor':50,'pedido':'PEDIDO4'}]

#Respostas

print(Manage(lista_motoboy, pedidos).respostas())



