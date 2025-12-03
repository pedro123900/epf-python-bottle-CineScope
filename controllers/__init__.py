from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.film_controller import film_routes 
from controllers.review_controller import review_routes

def init_controllers(app: Bottle):
    # Registra rotas de usuário
    app.merge(user_routes)
    app.merge(film_routes)
    
    # Registra rotas de filme
    print('🎬 Inicializando rotas de Filmes...')
    app.merge(film_routes) 

    print('⭐ Inicializando rotas de Reviews...')
    app.merge(review_routes)