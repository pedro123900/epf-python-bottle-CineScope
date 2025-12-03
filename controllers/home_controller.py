# controllers/home_controller.py
from bottle import Bottle, template, request
from models.film import Film  # Importando o Model que criamos

home_routes = Bottle()

@home_routes.route('/', method='GET')
def home():
    # Verifica cookie de login
    user_id = request.get_cookie("user_id", secret="minha_chave_secreta")
    
    # Busca os dados no "Banco" (Model)
    filmes_populares = Film.get_all()
    destaque_hero = Film.get_featured()

    # Renderiza a home enviando os dados reais
    return template('views/index_home', user_id=user_id, destaque=destaque_hero, filmes=filmes_populares)