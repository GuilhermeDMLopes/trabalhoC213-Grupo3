from tkinter import *
from tkinter import messagebox


class MinhaGUI:
    def __init__(self):
        # Criamos a janela principal
        self.janela_principal = Tk()

        # Criando os frames
        self.frame_cima = Frame(self.janela_principal)
        self.frame_baixo = Frame(self.janela_principal)

        # Criando label e botões do frame de cima
        self.label = Label(self.frame_cima, text='Digite seu nome:')

        # Criando o widget de entrada
        self.entrada = Entry(self.frame_cima, width=30)

        # Empacotando label e entrada no frame de cima
        self.label.pack(side='left')
        self.entrada.pack(side='left')

        # Criando os botões, no frame de baixo
        self.botao = Button(self.frame_baixo, text='Exibir', command=self.exibe)
        self.botao_sair = Button(self.frame_baixo, text='Sair', command=self.janela_principal.quit)

        # Empacotando os botões no frame de baixo
        self.botao.pack(side='left')
        self.botao_sair.pack(side='left')

        # Empacotando os botões janela principal
        self.botao.pack()
        self.botao_sair.pack()

        # Empacotando os frames na janela principal
        self.frame_cima.pack()
        self.frame_baixo.pack()

        # Rodando
        mainloop()

    def exibe(self):
        messagebox.showinfo('Python Progressivo', 'Seu nome é: ' + self.entrada.get())


gui = MinhaGUI()