from bottle import Bottle, request, redirect
from models.review import Review

review_routes = Bottle()

#ROTA DE POSTAR UMA AVALIAÇÃO
@review_routes.post('/reviews/adicionar')
def add_review():
    #pega o id do usuario logado
    user_id = request.get_cookie("user_id", secret="minha_chave_secreta")
    if not user_id:
        return redirect('/login')
    
    #pegar os dados do formulario 
    film_id = request.forms.get('film_id')
    rating = request.forms.get('rating')
    comment = request.forms.get('comment')

    #salva no banco
    Review.create(user_id, film_id, rating, comment)

    #volta pra pagina do filme(pra ver o review publicado)
    return redirect(f'/filmes/{film_id}')

#ROTA DE DELETAR AVALIACAO
@review_routes.get('/reviews/deletar/<review_id:int>')
def delete_review(review_id):
    #segurança
    user_id = request.get_cookie("user_id", secret="minha_chave_secreta")
    if not user_id:
        return redirect('/login')
    
    #tenta apagar (mas o model verifica se a review eh dele mesmo)
    #pra simplificar volta pra home depois de deletar
    Review.delete(review_id, user_id)

    return redirect('/')