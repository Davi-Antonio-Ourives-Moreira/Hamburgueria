from repository import Banco_Pedidos

class Pedidos(object):
    def __init__(self, nome, bairro, rua, n_residencia, pedido, pagamento, preco) -> None:
        self.pedidos_clientes = Banco_Pedidos()

        self.pedidos_clientes.Pedidos(nome_cliente=nome,
                                      bairro_cliente=bairro,
                                      rua_cliente=rua,
                                      numero_residencia_cliente=n_residencia,
                                      pedido_cliente=pedido,
                                      pagamento_cliente=pagamento,
                                      preco_pedido=preco
                                      )

