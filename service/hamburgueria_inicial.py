from repository import Banco_Recomendados
import flask

class Hamburgueria(object):
    def __init__(self) -> None:
        self.hamburguers = Banco_Recomendados()

        self.hamburguers_recomendados = self.hamburguers.Hamburguers_Recomendados()
    
    def Pagina_Inicial(self):
        
        return flask.render_template("index.html", recomendados=self.hamburguers_recomendados)