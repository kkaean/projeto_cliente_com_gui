import tkinter as tk  # Importa a biblioteca tkinter com o apelido "tk" para criar a janela e seus elementos (botões, caixas de texto, etc).

from Backend import Backend  # Importa o módulo Backend que tem as funções para salvar os nomes (a parte que cuida dos dados).

class Gui:  # Cria uma nova classe chamada Gui. Ela será usada para montar a tela com os botões, textos, etc.
    
    def __init__(self, master):  # Essa é a função que monta a tela. Ela é chamada quando a gente cria um Gui(root)
        self.master = master  # Guarda a janela principal (root) dentro da variável self.master
        self.master.title("Cadastro de Nomes")  # Define o título da janela
        self.master.geometry("600x350")  # Define o tamanho da janela (600 pixels de largura por 350 de altura)

        self.label = tk.Label(master, text="Digite seu nome:")  # Cria um texto que aparece na tela pedindo o nome
        self.label.pack(pady=5)  # Mostra esse texto na tela e dá um espaço de 5 pixels em cima e embaixo

        self.entry = tk.Entry(master)  # Cria uma caixinha onde o usuário pode digitar o nome
        self.entry.pack(pady=5)  # Mostra a caixinha na tela com um espacinho

        self.botao = tk.Button(master, text="Salvar", command=self.salvar_nome)  # Cria um botão com o texto "Salvar". Quando clicado, ele chama a função salvar_nome
        self.botao.pack(pady=10)  # Mostra o botão na tela com um pouco de espaço em volta

        self.mensagem = tk.Label(master, text="", fg="green")  # Cria um texto (inicialmente vazio) que vai mostrar mensagens como "Nome salvo!"
        self.mensagem.pack()  # Mostra esse rótulo (mesmo estando vazio no começo)

    def salvar_nome(self):  # Essa função é chamada quando o botão "Salvar" é clicado
        nome = self.entry.get()  # Pega o nome digitado na caixinha
        if nome.strip():  # Se o nome não estiver vazio (e não for só espaços em branco)...
            Backend.salvar_nome(nome)  # Chama a função do Backend para salvar esse nome
            self.mensagem.config(text="Nome salvo com sucesso!")  # Muda o texto da mensagem para avisar que deu certo
            self.entry.delete(0, tk.END)  # Limpa a caixinha de texto
        else:  # Se a pessoa não digitou nada...
            self.mensagem.config(text="Por favor, digite um nome.", fg="red")  # Mostra uma mensagem de erro em vermelho
