import sqlite3
import os

# Garante que estamos pegando o banco certo, não importa de onde você rode
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'data', 'cinescope.db')

def gerenciar_admin():
    if not os.path.exists(DB_PATH):
        print(f"❌ ERRO: Não achei o banco de dados em: {DB_PATH}")
        return

    print(f"🔌 Conectado em: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. LISTAR USUÁRIOS
    print("\n--- 👥 LISTA DE USUÁRIOS ---")
    cursor.execute("SELECT id, username, email, role FROM user")
    usuarios = cursor.fetchall()

    if not usuarios:
        print("O banco está vazio! Cadastre alguém pelo site primeiro.")
        return

    for u in usuarios:
        # u[0]=id, u[1]=nome, u[2]=email, u[3]=role
        icon = "👑" if u[3] == 'admin' else "👤"
        print(f"[ID: {u[0]}] {icon} {u[1]} ({u[2]}) - Cargo atual: {u[3]}")

    # 2. PERGUNTAR QUEM PROMOVER
    print("\n-----------------------------")
    try:
        target_id = input("Digite o NÚMERO do ID que você quer transformar em Admin: ")
        
        # Verifica se o ID existe
        cursor.execute("SELECT id FROM user WHERE id = ?", (target_id,))
        if not cursor.fetchone():
            print("❌ ID não encontrado.")
        else:
            # 3. EXECUTAR A PROMOÇÃO
            cursor.execute("UPDATE user SET role = 'admin' WHERE id = ?", (target_id,))
            conn.commit()
            print(f"\n✅ SUCESSO! O usuário de ID {target_id} agora é ADMIN supremo.")
            
    except ValueError:
        print("❌ Por favor, digite apenas números.")
    except Exception as e:
        print(f"❌ Erro: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    gerenciar_admin()