<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="\epf-python-bottle-CineScope\static\css\style_register.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="\epf-python-bottle-CineScope\static\img\icone_cinescope.png">

    <title>Registro CineScope</title>
</head>

<body>
    <main class="container">
        <form>
            <h1>
                <img src="\static\img\img_register.png" alt="Logo CineScope" class="icone-img">
                Registro CineScope</h1>
            <div class="input-box">
                <input placeholder="Usuário" type="text">
                <i class="bx bxs-user"></i>
            </div>
            <div class="input-box">
                <input placeholder="Email" type="email">
                <i class="bx bxl-gmail"></i>
            </div>
            <div class="input-box">
                <input placeholder="Digite sua senha" type="password">
                <i class="bx bxs-lock-alt"></i>
            </div>
            <div class="remember-me">
                <label>
                    <input type="checkbox">
                    Lembrar-me
                </label>
                <a href="">Esqueci minha senha</a>
            </div>
            <button type="submit">Registrar-me</button>

            <div class="login-link">
                <!--Configurar rota para a pagina de login!!-->
                <p>Já possui uma conta?</p><a href="">Clique aqui!</a>
            </div>
        </form>
    </main>
</body>

</html>