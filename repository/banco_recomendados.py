import psycopg2

class Banco_Recomendados(object):
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

    def Hamburguers_Recomendados(self):
        self.cursor.execute("SELECT * FROM hamburgues_recomendados")

        hamburguers = list(self.cursor.fetchall())

        return hamburguers