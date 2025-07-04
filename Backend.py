import sqlite3  # Importa a biblioteca sqlite3, que serve para criar e usar um banco de dados (como uma caixinha onde guardamos nomes)

class Backend:  # Cria uma classe chamada Backend, que vai cuidar de tudo que envolve salvar dados no banco de dados

    @staticmethod  # Diz que a função abaixo pode ser chamada sem precisar criar um objeto da classe
    def initDB():  # Esta função prepara o banco de dados (cria o arquivo e a tabela se ainda não existir)
        conexao = sqlite3.connect("nomes.db")  # Cria (ou abre) um arquivo de banco de dados chamado "nomes.db"
        cursor = conexao.cursor()  # Cria um "cursor", que é como um lápis que escreve dentro do banco de dados

        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                nome TEXT NOT NULL)  
        """) 
        
             # Manda um comando SQL para criar uma tabela chamada "pessoas", se ela ainda não existir
            # Cria uma coluna chamada "id" que aumenta sozinha a cada novo nome
            # Cria uma coluna chamada "nome" que não pode ficar vazia

        conexao.commit()  # Salva todas as mudanças feitas no banco de dados
        conexao.close()  # Fecha a conexão com o banco de dados (muito importante para não dar erro)

    @staticmethod  # Novamente, permite usar a função sem precisar criar um objeto
    def salvar_nome(nome):  # Esta função salva um nome dentro da tabela do banco de dados
        conexao = sqlite3.connect("nomes.db")  # Abre o banco de dados "nomes.db"
        cursor = conexao.cursor()  # Cria o cursor para escrever no banco

        cursor.execute("INSERT INTO pessoas (nome) VALUES (?)", (nome,))  # Insere o nome na tabela "pessoas"
        conexao.commit()  # Salva a mudança (o novo nome)
        conexao.close()  # Fecha o banco de dados
