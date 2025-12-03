<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>{{filme['titulo']}} - CineScope</title>
    <link rel="stylesheet" href="/static/css/style_home.css">
    <link rel="stylesheet" href="/static/css/style_forms.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>

<body>

    <header class="navbar">
        <div class="logo"><img src="/static/img/icone_cinescope.png"><span>CineScope</span></div>
        <nav class="menu"><a href="/">Home</a><a href="/catalogo">Catálogo</a></nav>
    </header>

    % background = filme.get('imagem', filme['poster'])
    <section class="hero"
        style="height: 80vh; background-image: linear-gradient(to bottom, rgba(20,24,28,0.2), #14181c), url('{{background}}');">
        <div class="hero-content">
            <h1 style="font-size: 60px;">{{filme['titulo']}}</h1>
            <div class="meta" style="font-size: 18px; margin-bottom: 20px;">
                <span>{{filme['ano']}}</span> • <span>Dirigido por {{filme['diretor']}}</span>
            </div>

            <p class="synopsis" style="max-width: 700px; font-size: 20px; line-height: 1.6;">
                {{filme['sinopse']}}
            </p>

            <div class="hero-buttons" style="margin-top: 30px;">
                <button id="openReviewBtn" class="btn-watch" style="background-color: #00e054; color: #14181c;">
                    <i class="bx bx-star"></i> Avalie esse Filme
                </button>
            </div>
        </div>
    </section>

    <main class="content-container" style="max-width: 900px;">
        <h2 style="border-bottom: 1px solid #333; padding-bottom: 15px; margin-bottom: 30px;">
            Reviews da Comunidade
        </h2>

        <div class="reviews-list" style="display: flex; flex-direction: column; gap: 20px;">
            % if len(reviews) > 0:
            % for review in reviews:
            <div class="review-card glass-effect"
                style="padding: 20px; border-radius: 10px; background: rgba(255,255,255,0.05);">
                <div class="review-header"
                    style="display: flex; justify-content: space-between; margin-bottom: 10px; color: #9ab;">
                    <div><i class="bx bxs-user-circle"></i> {{review['usuario']}}</div>
                    <div style="color: #00e054;">
                        % for i in range(int(review['nota'])):
                        ★
                        % end
                    </div>
                </div>
                <p style="color: #ddd;">"{{review['comentario']}}"</p>
            </div>
            % end
            % else:
            <p style="color: #666; font-style: italic;">Ninguém avaliou este filme ainda. Seja o primeiro!</p>
            % end
        </div>
    </main>

    <div id="reviewModal" class="modal-overlay">
        <div class="modal-content solid-background"
            style="width: 500px; padding: 40px; border-radius: 15px; background-color: #1f2429;">
            <span class="close-modal" id="closeReviewBtn">&times;</span>

            <form action="/filme/{{filme['id']}}/review" method="POST">
                <h2 style="margin-bottom: 5px; color: #fff;">Avaliar {{filme['titulo']}}</h2>
                <p style="color: #9ab; font-size: 13px; margin-bottom: 25px;">O que você achou?</p>

                <div class="form-group">
                    <label>Sua Nota</label>

                    <div class="star-rating" id="starsGeral">
                        <i class="bx bxs-star" onclick="avaliarGeral(1)"></i>
                        <i class="bx bxs-star" onclick="avaliarGeral(2)"></i>
                        <i class="bx bxs-star" onclick="avaliarGeral(3)"></i>
                        <i class="bx bxs-star" onclick="avaliarGeral(4)"></i>
                        <i class="bx bxs-star" onclick="avaliarGeral(5)"></i>
                    </div>

                    <input type="hidden" name="nota" id="inputNotaGeral" value="0" required>
                </div>

                <div class="form-group">
                    <label>Comentário</label>
                    <textarea name="comentario" placeholder="Escreva sua opinião..." required
                        style="height: 100px; background: #14181c; color: white; border: 1px solid #333; width: 100%; padding: 10px;"></textarea>
                </div>

                <button type="submit" class="btn-save"
                    style="width: 100%; padding: 15px; background-color: #00e054; color: #14181c; border: none; border-radius: 30px; font-weight: bold; cursor: pointer; margin-top: 15px;">
                    Publicar Review
                </button>
            </form>
        </div>
    </div>

    <script>
        const modal = document.getElementById("reviewModal");
        const btn = document.getElementById("openReviewBtn");
        const span = document.getElementById("closeReviewBtn");

        btn.onclick = function () { modal.style.display = "flex"; }
        span.onclick = function () { modal.style.display = "none"; }
        window.onclick = function (event) {
            if (event.target == modal) modal.style.display = "none";
        }
    </script>

    <footer style="margin-top: 100px; text-align: center; color: #555;">&copy; 2025 CineScope</footer>
</body>

</html>