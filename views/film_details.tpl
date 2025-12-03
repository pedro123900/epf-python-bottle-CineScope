<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{filme['titulo']}} - CineScope</title>
    <link rel="stylesheet" href="/static/css/style_home.css">
    <style>
        body { background-color: #14181c; color: white; font-family: sans-serif; margin: 0; }
        .hero {
            position: relative;
            height: 80vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }
        /* A imagem de fundo agora é uma tag IMG com posição absoluta */
        .hero-bg {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            object-fit: cover;
            z-index: -2;
            opacity: 0.6; /* Deixa um pouco escuro pra ler o texto */
        }
        .hero-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to bottom, rgba(20,24,28,0.5), #14181c);
            z-index: -1;
        }
        .hero-content { position: relative; z-index: 1; text-align: center; max-width: 800px; padding: 20px; }
        .btn-watch {
            padding: 15px 30px; border: none; border-radius: 30px;
            font-size: 16px; font-weight: bold; cursor: pointer;
            display: inline-flex; align-items: center; gap: 10px;
        }
    </style>
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>

<body>

    <header class="navbar" style="padding: 20px; display: flex; align-items: center; justify-content: space-between; background: rgba(0,0,0,0.8); position: fixed; top: 0; width: 100%; z-index: 100;">
        <div class="logo" style="display: flex; align-items: center; gap: 10px; font-weight: bold; font-size: 20px;">
            <img src="/static/img/icone_cinescope.png" style="height: 30px;"><span>CineScope</span>
        </div>
        <nav class="menu" style="display: flex; gap: 20px;">
            <a href="/" style="color: white; text-decoration: none;">Home</a>
            <a href="/" style="color: white; text-decoration: none;">Catálogo</a>
        </nav>
    </header>

    <section class="hero">
        <img src="{{filme['imagem']}}" class="hero-bg" onerror="this.src='{{filme['poster']}}'">
        <div class="hero-overlay"></div>

        <div class="hero-content">
            <img src="{{filme['poster']}}" style="height: 200px; border-radius: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 20px;">
            <h1 style="font-size: 50px; margin: 0;">{{filme['titulo']}}</h1>
            <div class="meta" style="font-size: 18px; margin: 20px 0; color: #ccc;">
                <span>{{filme['ano']}}</span> • <span>Dirigido por {{filme['diretor']}}</span>
            </div>

            <p class="synopsis" style="font-size: 18px; line-height: 1.6; color: #ddd;">
                {{filme['sinopse']}}
            </p>

            <div class="hero-buttons" style="margin-top: 30px;">
                <button id="openReviewBtn" class="btn-watch" style="background-color: #00e054; color: #14181c;">
                    <i class="bx bx-star"></i> Avalie esse Filme
                </button>
            </div>
        </div>
    </section>

    <main style="max-width: 800px; margin: 0 auto; padding: 40px 20px;">
        <h2 style="border-bottom: 1px solid #333; padding-bottom: 15px; margin-bottom: 30px;">
            Reviews da Comunidade
        </h2>

        <div style="display: flex; flex-direction: column; gap: 20px;">
            % if len(reviews) > 0:
                % for review in reviews:
                <div style="padding: 20px; border-radius: 10px; background: rgba(255,255,255,0.05); border: 1px solid #333;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px; color: #9ab;">
                        <div style="font-weight: bold;"><i class="bx bxs-user-circle"></i> {{review['usuario']}}</div>
                        <div style="color: #00e054;">
                            % for i in range(int(review['nota'])):
                            ★
                            % end
                        </div>
                    </div>
                    <p style="color: #eee; margin: 0;">"{{review['comentario']}}"</p>
                    <small style="color: #666; display: block; margin-top: 10px;">{{review['data']}}</small>
                </div>
                % end
            % else:
                <p style="color: #666; font-style: italic; text-align: center;">Ninguém avaliou este filme ainda. Seja o primeiro!</p>
            % end
        </div>
    </main>

    <div id="reviewModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 200; justify-content: center; align-items: center;">
        <div style="width: 500px; padding: 40px; border-radius: 15px; background-color: #1f2429; position: relative;">
            <span id="closeReviewBtn" style="position: absolute; top: 15px; right: 20px; font-size: 30px; cursor: pointer; color: #aaa;">&times;</span>

            <form action="/filme/{{filme['id']}}/review" method="POST">
                <h2 style="margin-top: 0; color: white;">Avaliar {{filme['titulo']}}</h2>
                
                <label style="display: block; margin-top: 20px; color: #ccc;">Nota (1 a 5):</label>
                <input type="number" name="nota" min="1" max="5" value="5" style="width: 100%; padding: 10px; margin-top: 5px; background: #14181c; border: 1px solid #333; color: white; border-radius: 5px;" required>

                <label style="display: block; margin-top: 20px; color: #ccc;">Comentário:</label>
                <textarea name="comentario" rows="4" style="width: 100%; padding: 10px; margin-top: 5px; background: #14181c; border: 1px solid #333; color: white; border-radius: 5px;" required></textarea>

                <button type="submit" style="width: 100%; padding: 15px; background-color: #00e054; color: #14181c; border: none; border-radius: 30px; font-weight: bold; cursor: pointer; margin-top: 25px;">
                    Publicar Review
                </button>
            </form>
        </div>
    </div>

    <script>
        const modal = document.getElementById("reviewModal");
        const btn = document.getElementById("openReviewBtn");
        const span = document.getElementById("closeReviewBtn");

        if(btn) btn.onclick = function() { modal.style.display = "flex"; }
        if(span) span.onclick = function() { modal.style.display = "none"; }
        window.onclick = function(event) {
            if (event.target == modal) modal.style.display = "none";
        }
    </script>
</body>
</html>