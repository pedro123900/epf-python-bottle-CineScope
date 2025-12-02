from app import create_app

if __name__ == '__main__':
    #Cria a aplicação usando a classe App d
    app = create_app()
    
    # 2. Roda o servidor
    print("🚀 Servidor iniciando...")
    app.run()