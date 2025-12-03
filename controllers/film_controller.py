from bottle import Bottle, request, redirect, template
from models.film import Film
from models.review import Review
from models.user import User

film_routes = Bottle()

# --- HELPER: Tradutor ---
def to_vitin_film(film_obj):
    return {
        'id': film_obj.id,
        'titulo': film_obj.title,
        'diretor': film_obj.director,
        'ano': film_obj.year,
        'poster': film_obj.poster_image,
        'imagem': film_obj.poster_image,
        'sinopse': "Sinopse indisponível." 
    }

def to_vitin_review(review_obj):
    return {
        'usuario': review_obj.username,
        'nota': review_obj.rating,
        'comentario': review_obj.comment,
        'data': review_obj.created_at
    }

# --- ROTA HOME ---
@film_routes.get('/')
def home():
    user_id = request.get_cookie("user_id", secret="minha_chave_secreta")
    if not user_id: return redirect('/login')

    filmes_objs = Film.find_all()
    filmes_dict = [to_vitin_film(f) for f in filmes_objs]

    if filmes_dict:
        destaque = filmes_dict[0]
    else:
        destaque = {
            'id': 0, 'titulo': 'Bem-vindo', 'ano': '2025', 
            'sinopse': 'Cadastre filmes!', 'imagem': '/static/img/background_placeholder.jpg'
        }

    return template('views/index_home', filmes=filmes_dict, destaque=destaque, user_id=user_id)

# --- ROTA DETALHES (COM DEBUG) ---
@film_routes.get('/filme/<film_id:int>')
def film_details(film_id):
    if not request.get_cookie("user_id", secret="minha_chave_secreta"):
        return redirect('/login')

    print(f"👀 TENTANDO ABRIR O FILME ID: {film_id}") # DEBUG

    # Busca dados
    filme_obj = Film.find_by_id(film_id)
    
    if not filme_obj:
        print(f"❌ ERRO: O Model retornou Vazio (None) para o ID {film_id}") # DEBUG
        return redirect('/')
    
    print(f"✅ SUCESSO: Filme encontrado: {filme_obj.title}") # DEBUG

    reviews_objs = Review.find_by_film_id(film_id)
    
    # Traduz dados
    filme_dict = to_vitin_film(filme_obj)
    reviews_dict = [to_vitin_review(r) for r in reviews_objs]

    return template('views/film_details', filme=filme_dict, reviews=reviews_dict)

# ... (Mantenha as rotas de Admin iguais) ...
@film_routes.get('/admin/filmes')
def add_film_form():
    user_id = request.get_cookie("user_id", secret="minha_chave_secreta")
    if not user_id: return redirect('/login')
    user = User.find_by_id(user_id)
    if not user or user['role'] != 'admin': return redirect('/') 
    return template('views/film_form')

@film_routes.post('/admin/filmes')
def add_film_submit():
    user_id = request.get_cookie("user_id", secret="minha_chave_secreta")
    if not user_id: return redirect('/login')
    user = User.find_by_id(user_id)
    if not user or user['role'] != 'admin': return redirect('/')

    titulo = request.forms.get('titulo')
    diretor = request.forms.get('diretor')
    ano = request.forms.get('ano')
    poster = request.forms.get('poster')
    
    Film.create(titulo, diretor, ano, poster)
    return redirect('/')