from bottle import Bottle, static_file # Importante static_file tem que estar aqui
from config import Config

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()

    def setup_routes(self):
        # importa e inicializa os controllers (Login, Cadastro, etc)
        from controllers import init_controllers
        print('🚀 Inicializa rotas de Usuário...')
        init_controllers(self.bottle)

        # ROTA DE ARQUIVOS ESTÁTICOS (CSS/IMG) 
        @self.bottle.route('/static/<filepath:path>')
        def server_static(filepath):
            # O './static' faz com que que ele procure na pasta static da raiz
            return static_file(filepath, root='./static')

    def run(self):
        self.setup_routes()
        
        # Inicia o servidor
        self.bottle.run(
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )

def create_app():
    return App()