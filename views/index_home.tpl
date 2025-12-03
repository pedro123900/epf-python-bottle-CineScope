<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CineScope - Home</title>
    <link rel="stylesheet" href="/static/css/style_home.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>

    <header class="navbar">
        <div class="logo">
            <img src="/static/img/icone_cinescope.png" alt="Logo">
            <span>CineScope</span>
        </div>
        
        <nav class="menu">
            <a href="/">Filmes</a>
            <a href="#">Membros</a>
        </nav>

        <div class="search-bar">
            <i class="bx bx-search"></i>
            <input type="text" placeholder="Buscar filmes...">
        </div>

        <div class="user-actions">
            % if user_id:
                <a href="/profile" class="user-icon"><i class="bx bxs-user-circle"></i></a>
                <a href="/logout" class="btn-action">Sair</a>
            % else:
                <a href="/login" class="btn-login">Login</a>
                <a href="/register" class="btn-register">Criar Conta</a>
            % end
        </div>
    </header>

    <section class="hero" style="background-image: linear-gradient(to bottom, rgba(0,0,0,0.3), #14181c), url('{{destaque['imagem']}}');">
        <div class="hero-content">
            <h1>{{destaque['titulo']}}</h1>
            <div class="meta">
                <span>{{destaque['ano']}}</span>
            </div>
            <p class="synopsis">{{destaque['sinopse']}}</p>
            
            <div class="hero-buttons">
                % if destaque['id'] == 0:
                    <a href="/admin/filmes" style="text-decoration: none;">
                        <button class="btn-watch" style="background-color: #00e054; color: #14181c; cursor: pointer;">
                            <i class="bx bx-plus-circle"></i> Começar Catálogo (Admin)
                        </button>
                    </a>
                % else:
                    <a href="/filme/{{destaque['id']}}" style="text-decoration: none;">
                        <button class="btn-watch" style="cursor: pointer;">
                            <i class="fa-solid fa-circle-info"></i> Mais Informações
                        </button>
                    </a>
                    
                    <button class="btn-list"><i class="fa-solid fa-plus"></i> Watchlist</button>
                % end
            </div>
        </div>
    </section>

    <main class="content-container">
        <div class="section-header">
            <h2>Catálogo</h2>
            <a href="/catalogo">Ver todos</a>
        </div>

        <div class="movies-grid">
            % for filme in filmes:
            <a href="/filme/{{filme['id']}}" class="movie-card">
                <div class="poster" style="background-image: url('{{filme['poster']}}');">
                    <div class="overlay">
                        <i class="fa-solid fa-eye"></i>
                        <i class="fa-solid fa-heart"></i>
                    </div>
                </div>
            </a>
            % end
        </div>
        
        <div class="section-header" style="margin-top: 50px;">
            <h2>Reviews Recentes</h2>
        </div>
        <div class="reviews-list">
             <div class="review-card glass-effect">
                <div class="review-header">
                    <i class="bx bxs-user-circle"></i> <span>Usuário123</span>
                    <span class="stars">★★★★★</span>
                </div>
                <p>Absolutamente incrível! A cinematografia é de outro mundo.</p>
                <small>Assistiu: Wicked</small>
             </div>
        </div>
    </main>

    <footer>
        <p style="text-align: center; color: #555; font-size: 12px; margin-top: 50px; padding-bottom: 20px;">
            &copy; 2025 CineScope. 
            <br><br>
            <a href="/admin/filmes" style="color: #333; text-decoration: none;">Acesso Admin</a>
        </p>
    </footer>
</body>
</html>