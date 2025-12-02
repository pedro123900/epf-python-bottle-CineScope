import sqlite3 
import os
#pelo que vi o "os" seria pra garantir o funcionamento do sistema em qualquer pc (linux)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "cinescope.db")

def get_connection():
    #pega uma conexão do banco, sempre vai ser usada se precisar ler ou salvar dados
    conn = sqlite3.connect(DB_PATH)
    #permite acessar colunas pelo nome
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    #cria as tabelas necessarias se elas ainda nao existirem
    conn = get_connection()
    cursor = conn.cursor()

    print(f"Criando banco de dados em {DB_PATH}")

    #Tabela 1: Usuarios
    #"role" define se é admin ou regular
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT NOT NULL,
           email TEXT NOT NULL UNIQUE,
           password_hash TEXT NOT NULL,
           role TEXT DEFAULT 'regular',
           created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
           )
    ''')

    #Tabela 2: Filmes 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS film(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            director TEXT NOT NULL,
            year INTEGER,
            poster_image TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
    ''')

    #Tabela 3: Reviews(Liga Usuario + Filme)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS review (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            film_id INTEGER NOT NULL,
            rating INTEGER NOT NULL,
            comment TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES user (id),
            FOREIGN KEY (film_id) REFERENCES film (id)
            )
    ''')

    #Tabela 4: Wishlist(Tabela de juncao N-N)
    #Guarda quais filmes o usuario quer ver
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wishlist (
            user_id INTEGER NOT NULL,
            film_id INTEGER NOT NULL,
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (user_id, film_id),
            FOREIGN KEY (user_id) REFERENCES user (id),
            FOREIGN KEY (film_id) REFERENCES film (id)
            )
    ''')

    conn.commit()
    conn.close()
    print("Tabelas criadas!")

    #aqui ele ja cria as tabelas direto
if __name__ == '__main__':
    create_tables()