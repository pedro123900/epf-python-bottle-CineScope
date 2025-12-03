from bottle import Bottle, request, redirect
from models.review import Review

#cria o departamento de reviews
review_routes = Bottle()

#ROTA POSTAR REVIEW
@review_routes.post('/filme/<film_id:int>/review')
def add_review(film_id):
    #pega o user id do cookie
    user_id = request.get_cookie("user_id", secret="minha_chave_secreta")
    
    #seguranca basica
    if not user_id:
        return redirect('/login')

    #pega os dados do formulario 
    rating = request.forms.get('nota')
    comment = request.forms.get('comentario')

    #salva no banco
    Review.create(user_id, film_id, rating, comment)

    #volta para a pagina do filme atualizada
    return redirect(f'/filme/{film_id}')

#ROTA DELETAR REVIEW  (caso precisexxxxxxxxx    
@review_routes.get('/reviews/deletar/<review_id:int>')
def delete_review(review_id):
    user_id = request.get_cookie("user_id", secret="minha_chave_secreta")
    if user_id:
        Review.delete(review_id, user_id)
    return redirect('/')