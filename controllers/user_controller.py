from bottle import Bottle, request, redirect, response, template
from models.user import User
import hashlib

# CRIA O OBJETO "user_routes" 
user_routes = Bottle()

# ROTA DE CADASTRO 
@user_routes.get('/register')
def register_form():
    # fui mais direto com o endereço (views)
    return template('views/index_register')

@user_routes.post('/register')
def register_submit():
    username = request.forms.get('username') # No HTML o name="username"
    email = request.forms.get('email')       # No HTML o name="email"
    password = request.forms.get('password') # No HTML o name="password"

    # Tenta criar o usuário
    sucesso = User.create(username, email, password)

    if sucesso:
        return redirect('/login')
    else:
        # Retorna erro usando o template certo
        return template('views/index_register', error="Email já cadastrado!")

# ROTA DE LOGIN

@user_routes.get('/login')
def login_form():
    # Verifica o cookie
    if request.get_cookie("user_id", secret="minha_chave_secreta"):
        return redirect('/')
    
    # Chama o template certo (index_login.tpl)
    return template('views/index_login')

@user_routes.post('/login')
def login_submit():
    email = request.forms.get('email')
    password = request.forms.get('password')

    user = User.find_by_email(email)

    if user:
        # criptografa a senha colocada pra comparar com a original
        hashed_input = hashlib.sha256(password.encode()).hexdigest()

        if hashed_input == user['password_hash']:
            # Senha correta: cria o cookie
            response.set_cookie("user_id", str(user['id']), secret="minha_chave_secreta")
            return redirect('/') 
        
    # Se der erro
    return template('views/index_login', error="Email ou senha incorretos.")

#ROTA DE LOGOUT

@user_routes.get('/logout')
def logout():
    response.delete_cookie("user_id")
    return redirect('/login')
    

#ROTA RAIZ (HOME)
