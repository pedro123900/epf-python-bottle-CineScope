from bottle import Bottle, request, redirect, response, template
from models.film import Film
from models.review import Review
from models.user import User

#cria o departamento de filmes
film_routes = Bottle()

#ROTA HOME / CATALOGO (lista para todos os filmes)
@film_routes.get('/')
def home():
    #so entra se tiver o cookie user id
    if not request.get_cookie("user_id", secret="minha_chave_secreta"):
        return redirect('/login')
    
    #busca todos os filmes do banco e o model devolve uma lista de objetos FIlm
    filmes = Film.find_all()

    #manda a lista pro HTML
    return template('views/index_home', filmes=filmes)

#ROTA DETALHES DO FILME + REVIEW
@film_routes.get('/filmes/<film_id:int>')
def film_details(film_id):
    #seguranca
    if not request.get_cookie("user_id", secret="minha_chave_secreta"):
        return redirect('/login')
    
    #busca o filme pelo id
    filme = Film.find_by_id(film_id)

    #busca as reviews desse filme
    reviews = Review.find_by_film_id(film_id)

    #se o filme nao existir volta pra home
    if not filme:
        return redirect('/')
    
    return template('views/film_details', filme=filme, reviews=reviews)




#ROTA da tela de add filmes
@film_routes.get('/filmes/adicionar')
def add_film_form():
    if not request.get_cookie("user_id", secret="minha_chave_secreta"):
        return redirect('/login')
    
    #pega os dados do usuario pra checar o admin
    user = User.find_by_id(user_id)
    
    #verificaçõa de admin 
    #se nao for admin joga ele pra home
    if not user or user['role'] != 'admin':
        return redirect('/')

    return template('views/films_form')


#ROTA processar a adição de filme
@film_routes.post('/filmes/adicionar')
def add_film_submit():
    if not request.get_cookie("user_id", secret="minha_chave_secreta"):
        return redirect('/login')
    
    #verifica se eh admin denovo
    user = User.find_by_id
    if not user or user['role'] != 'admin':
        return redirect('/')

    
    #pega os dados do formulario 
    title = request.forms.get('title')
    director = request.forms.get('director')
    year = request.forms.get('year')
    poster_image = request.forms.get('poster_image')

    #faz o model salvar
    sucesso = Film.create(title, director, year, poster_image)

    if sucesso:
        return redirect('/')
    else:
        return template('views/films_form', error="Erro ao cadastrar filme!")
