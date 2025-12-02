from bottle import Bottle, request, redirect, response, template, static_file
from models.user import User
import hashlib

# definindo a app do bottle para as rotas de usuario
user_routes = Bottle()

# ROTA DE CADASTRO

@user_routes.get('/cadastro')
def register_form():
    #exibir a pagina html de cadastro
    return template('index_register')


@user_routes.post('/cadastro')
def register_submit():
    #pega os dados que foram mandados pelo formulario 
    username = request.forms.get('username')
    email = request.forms.get('email')
    password = request.forms.get('password')

    #chama o model para tentar salvar no banco 
    sucesso = User.create(username, email, password)

    if sucesso:
        #se deu certo manda pro login
        return redirect('/login')
    else:
        #se deu erro avisa na tela (email ja usado)
        return template('index_register', error = "Email ja cadastrado!")
    
    
#ROTA DE LOGIN


@user_routes.get('/login')
def login_form():
    #se o usuario ja estiver logado joga ele pra home direto
    if request.get_cookie("user_id", secret="minha_chave_secreta"):
        return redirect('/')
    return template('index_login')

@user_routes.post('/login')
def login_submit():
    email = request.forms.get('email')
    password = request.forms.get('password')

    #busca o usuario no banco pelo email
    user = User.find_by_email(email)

    if user:
        #verifica a senha
        #pega a senha que ele digitou AGORA, decodifica e compara com a do banco
        hashed_input = hashlib.sha256(password.encode()).hexdigest()

        if hashed_input == user['password_hash']:
            #senha correta
            #cria um cookie pro navegador lembrar dele
            response.set_cookie("user_id", str(user['id']), secret= "minha_chave_secreta")
            return redirect('/') # manda pra home
        
    #se ta aqui eh pq errou email ou senha
    return template('index_login', error = "Email ou senha incorretos.")

#ROTA DE LOGOUT

@user_routes.get('/logout')
def logout():
    #apaga o cookie do usuario
    response.delete_cookie("user_id")
    return redirect('/login')      


#rota para arquivos estaticos (CSS, imagens etc)
@user_routes.get('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')