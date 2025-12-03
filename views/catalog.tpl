<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Catálogo Completo - CineScope</title>
    <link rel="stylesheet" href="/static/css/style_home.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <header class="navbar">
        <div class="logo"><img src="/static/img/icone_cinescope.png"><span>CineScope</span></div>
        <nav class="menu">
            <a href="/">Home</a>
            <a href="/catalogo" style="color: white;">Catálogo</a>
        </nav>
        </header>

    <main class="content-container" style="padding-top: 100px;">
        <h1 style="margin-bottom: 30px; border-bottom: 1px solid #333; padding-bottom: 10px;">Todos os Filmes</h1>
        
        <div class="movies-grid">
            % for filme in filmes:
            <a href="/filme/{{filme['id']}}" class="movie-card">
                <div class="poster" style="background-image: url('{{filme['poster']}}');">
                    <div class="overlay"><i class="fa-solid fa-eye"></i></div>
                </div>
                <h3 style="margin-top: 10px; font-size: 14px; color: #ccc;">{{filme['titulo']}}</h3>
            </a>
            % end
        </div>
    </main>
</body>
</html>