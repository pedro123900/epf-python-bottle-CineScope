<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="stylesheet" href="/static/css/style.css">
    <link rel="stylesheet" href="/static/css/style_login.css">
    
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'> 
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <link rel="icon" href="/static/img/icone_cinescope.png" type="image/png">
    
    <title>Login - CineScope</title>
</head>
<body>
    <main class="container">
        <form>
            <h1>
                <img src="/static/img/icone_cinescope.png" alt="Logo CineScope" class="icone-img">
                CineScope Login
            </h1>
            <div class="input-box">
                <input placeholder="Usuário" type="email">
                <i class="bx bxs-user"></i>
            </div>
            <div class="input-box">
                <input placeholder="Senha" type="password">
                <i class="bx bxs-lock-alt"></i>
                
            </div>
            <div class="remember-forgot">
                <label>
                <input type="checkbox">
                Lembrar-me
                </label>
                <!--lembre de colocar um link para o esqueci minha senha no href-->
                <a href="#">Esqueci minha senha</a>
            </div>
            <button type="submit" class="login">Login</button>
            <div>
                <!--Colocar um link para a pagina de cadastro no Clique aqui-->
                <p>Não tenho uma conta. <a href="#">Clique aqui</a></p>
            </div>
        </form>
            


    </main>
</body>
</html>