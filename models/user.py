import sqlite3
import hashlib
from data.database import get_connection


class User:
    def __init__(self, id, username, email, password_hash, role='regular'):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role

    @staticmethod
    def create(username, email, password):
        #cria um novo usuario do banco de dados, retorna True se der certo, e False se o email ja existir

        #1- criptografa a senha antes de salvar
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = get_connection()
        cursor = conn.cursor()

        #tratamento de erro
        try:
            cursor.execute('''
                INSERT INTO user (username, email, password_hash)
                VALUES (?, ?, ?)
            ''', (username, email, hashed_password))

            conn.commit()
            return True
        except sqlite3.IntegrityError:
            #Erro, o email ja existe no banco
            return False
        finally:
            conn.close()
            
    @staticmethod
    def find_by_email(email):
        #busca um usuario pelo email(para login) e retorna os dados do usuario ou None se nao achar
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT *  FROM user WHERE email = ?', (email,))
        user_data = cursor.fetchone()

        conn.close()

        if user_data:
            return user_data
        else:
            return None
    
    @staticmethod
    def find_by_id(user_id):
        #Busca pelo ID( util se o usuario ja tiver logado)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM user WHERE id = ?', (user_id))
        user = cursor.fetchone()

        conn.close()
        return user

            