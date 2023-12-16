import psycopg2

class Banco_Pedidos(object):
    def __init__(self) -> None:
        self.host ='localhost'
        self.dbname = 'hamburgueria'
        self.user = 'postgres'
        self.password = 'postgres'
        self.port = 5432

        self.conectar = psycopg2.connect(user=self.user,
                                         password=self.password,
                                         host=self.host,
                                         port=self.port,
                                         dbname=self.dbname
                                         )
        
        self.cursor = self.conectar.cursor()

    def Pedidos(self, nome_cliente, bairro_cliente, rua_cliente, numero_residencia_cliente, pedido_cliente, pagamento_cliente, preco_pedido):
        self.cursor.execute("INSERT INTO pedidos (nome_pessoa, bairro_pessoa, rua_pessoa, numero_residencia, hamburguer_pedido, pagamento, preco_hamburguer) VALUES (%s, %s, %s, %s, %s, %s, %s);", (nome_cliente, bairro_cliente, rua_cliente, numero_residencia_cliente, pedido_cliente, pagamento_cliente, preco_pedido))
        
        self.conectar.commit()
    
    def C(self):
        self.cursor.execute("CREATE TABLE dadaaa(nome text, senha text)")

        self.conectar.commit()
        

    def Pegar_Valores_Hamburguer(self, nome_hamburguer):
        self.cursor.execute("SELECT * FROM  hamburgues_recomendados WHERE hamburguer=%s", (nome_hamburguer, ))

        self.valores_hamburguers = self.cursor.fetchall()

        return self.valores_hamburguers