import tkinter as tk  # Importa a biblioteca "tkinter" e dá o apelido "tk" para usá-la mais fácil. Ela serve para criar janelas, botões e outros elementos gráficos.

from Gui import Gui  # Importa a classe chamada "Gui" que está dentro do arquivo "Gui.py". Essa classe cuida da parte gráfica (o que aparece na tela).

from Backend import Backend  # Importa o módulo "Backend" que está no arquivo "Backend.py". Esse módulo cuida da parte de trás do programa, como salvar dados ou mexer no banco de dados.

def main():  # Define (cria) a função principal do programa. Tudo começa aqui quando o programa roda.
    Backend.initDB()  # Chama a função "initDB()" do Backend, que provavelmente prepara o banco de dados (cria a tabela, conecta, etc).
    
    root = tk.Tk()  # Cria a janela principal do programa usando tkinter.
    
    app = Gui(root)  # Cria a interface gráfica (botões, rótulos, etc) usando a classe Gui, e coloca tudo dentro da janela "root".
    
    root.mainloop()  # Faz a janela ficar aberta esperando o usuário clicar nos botões ou fechar a janela.

if __name__ == "__main__":  # Verifica se o arquivo está sendo executado diretamente (e não importado de outro lugar).
    main()  # Se for o caso, chama a função main() para iniciar o programa.
