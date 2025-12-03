import sqlite3
from data.database import get_connection

class Film:
    def __init__(self, id, title, director, year, poster_image):
        self.id = id
        self.title = title
        self.director = director
        self.year = year
        self.poster_image = poster_image

    @staticmethod
    def create(title, director, year, poster_image):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO film (title, director, year, poster_image)
                VALUES (?, ?, ?, ?)
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
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM film ORDER BY created_at DESC')
        films_data = cursor.fetchall()
        conn.close()

        films_list = []
        for row in films_data:
            film = Film(
                id=row['id'],
                title=row['title'],
                director=row['director'],
                year=row['year'],
                poster_image=row['poster_image']
            )
            films_list.append(film)
        return films_list

    @staticmethod
    def find_by_id(film_id):
        conn = get_connection()
        cursor = conn.cursor()
        
        # Busca o filme pelo ID
        cursor.execute('SELECT * FROM film WHERE id = ?', (film_id,))
        row = cursor.fetchone()
        conn.close()

        # Se achou, retorna o Objeto Film
        if row:
            return Film(
                id=row['id'], 
                title=row['title'], 
                director=row['director'], 
                year=row['year'], 
                poster_image=row['poster_image']
            )
        # Se não achou, retorna None (isso que faz voltar pra Home)
        return None