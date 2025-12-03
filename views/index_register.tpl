<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/style_register.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <title>Registro CineScope</title>
</head>

<body>
    <main class="container">
        <form action="/register" method="POST">
            <h1>
                <img src="/static/img/icone_cinescope.png" alt="Logo CineScope" class="icone-img">
                Registro CineScope
            </h1>

            % if defined('error'):
                <p style="color: #ff4444; text-align: center; margin-bottom: 10px; font-weight: bold;">{{error}}</p>
            % end

            <div class="input-box">
                <input name="username" placeholder="Usuário" type="text" required>
                <i class="bx bxs-user"></i>
            </div>
            
            <div class="input-box">
                <input name="email" placeholder="Email" type="email" required>
                <i class="bx bxl-gmail"></i>
            </div>
            
            <div class="input-box">
                <input name="password" placeholder="Digite sua senha" type="password" required>
                <i class="bx bxs-lock-alt"></i>
            </div>
            
            <div class="remember-me">
                <label>
                    <input type="checkbox"> Lembrar-me
                </label>
                <a href="#">Esqueci minha senha</a>
            </div>
            
            <button type="submit">Registrar-me</button>

            <div class="login-link">
                <p>Já possui uma conta? <a href="/login">Clique aqui!</a></p>
            </div>
        </form>
    </main>
</body>
</html>