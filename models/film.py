import sqlite3
from data.database import get_connection    

class Film:
    def __init__(self, id, title, director, year, poster_image):
        self.id = id
        self.title = title
        self.director = director
        self.year= year
        self.poster_image = poster_image

    @staticmethod
    def create(title, director, year, poster_image):
        #salva um novo filme no banco de dados (implementar so adm conseguirem fazer isso)

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT INTO film ( title, director, year, poster_image)
                VALUES(?, ?, ?, ?)

            ''', (title, director, year, poster_image))

            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao criar filme: {e}")
            return False
        finally:
            conn.close()
        

    @staticmethod
    def find_all():
        #retorna todos os filmes cadastrados e sera usado pra preencher a pagina home

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM  film ORDER BY created_at DESC')
        films_data = cursor.fetchall() #pega uma lista de filmes

        conn.close()

        #como o banco vai devolver em linhas, vou transformar em objetos film ou dicionarios pra facilitar o HTML
        films_list = []
        for row in films_data:
            #converte cada linha do banco em objeto film
            film = Film(
                id = row['id'],
                title= row['title'],
                director=row['director'],
                year=row['year'],
                poster_image=row['poster_image']
            )
            films_list.append(film)
        return films_list
    

    @staticmethod
    def find_by_id(film_id):
        #busca um filme especifico pelo id
        #vai ser usado quando clicar no filme para ver detalhes do mesmo

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT FROM film WHERE id = ?', (film_id))
        row = cursor.fetchone()

        conn.close()
        
        if row:
            return Film(
                id=row['id'],
                title=row['title'],
                director=row['director'],
                year=row['year'],
                poster_image=row['poster_image']
            )
        return None
