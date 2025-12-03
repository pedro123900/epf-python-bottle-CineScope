import sqlite3
from data.database import get_connection

class Review:
    def __init__(self, id, user_id, film_id, rating, comment, created_at, username=None):
        self.id = id
        self.user_id = user_id
        self.film_id = film_id
        self.rating = rating
        self.comment = comment
        self.created_at = created_at
        #username aqui eh um campo extra pra facilitar na tela a exibicao (quem comentou)
    
    @staticmethod
    def create(user_id, film_id, rating, comment):
        #salva uma nova avaliação no banco

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT INTO review (user_id, film_id, rating, comment)
                VALUES (?, ?, ?, ?)
            ''', (user_id, film_id, rating, comment))
        
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao salvar review: {e}")
            return False
        finally:
            conn.close()

    
    @staticmethod
    def find_by_film_id(film_id):
        #busca todas as reviews de um filme especifico
        #faz um JOIN com a tabela de usuarios pra saber quem ja comentou

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT r.*, username
            FROM review r
            JOIN user u ON r.user_id = u.id
            WHERE r.film_id = ?
            ORDER BY r.created_at DESC
        ''', (film_id))

        reviews_data = cursor.fetchall()
        conn.close()

        reviews_list = []
        for row in reviews_data:
            reviews_list.append(Review(
                id=row['id'],
                user_id=row['user_id'],
                film_id=row['film_id'],
                rating=row['rating'],
                comment=row['comment'],
                created_at=row['created_at'],
                username=row['username'] #preenche o nome aqui
            ))
        
        return reviews_list
    
    @staticmethod
    def delete(review_id, user_id):
        #apaga uma review, e verifica se o usuario tentando apagar é o dono da review

        conn = get_connection
        cursor = conn.cursor()

        #primeiro verifica se eh do usuario
        cursor.execute('SELECT id FROM review WHERE id = ? AND user_id = ?', (review_id, user_id))
        if not cursor.fetchone():
            conn.close()
            return False #nao achou ou nao eh o dono
        
        cursor.execute('DELETE FROM review WHERE id = ?', (review_id))
        conn.commit()
        conn.close()
        return True