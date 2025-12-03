<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/style_login.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <title>Login - CineScope</title>
</head>
<body>
    <main class="container">
        <form action="/login" method="POST">
            <h1>
                <img src="/static/img/icone_cinescope.png" alt="Logo CineScope" class="icone-img">
                CineScope Login
            </h1>
            
            % if defined('error'):
                <div style="background-color: #ff4444; color: white; padding: 10px; border-radius: 5px; margin-bottom: 15px; text-align: center;">
                    {{error}}
                </div>
            % end

            <div class="input-box">
                <input name="email" placeholder="Email" type="email" required>
                <i class="bx bxs-user"></i>
            </div>
            
            <div class="input-box">
                <input name="password" placeholder="Senha" type="password" required>
                <i class="bx bxs-lock-alt"></i>
            </div>

            <div class="remember-forgot">
                <label><input type="checkbox"> Lembrar-me</label>
                <a href="#">Esqueci minha senha</a>
            </div>

            <button type="submit" class="login">Login</button>
            
            <div class="register-link">
                <p>Não tenho uma conta. <a href="/register">Clique aqui</a></p>
            </div>
        </form>
    </main>
</body>
</html>