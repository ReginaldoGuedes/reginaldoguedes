import customtkinter as ctk
from tkinter import *
import database
from sqlite3 import Error
from tkinter import messagebox

"""
Para que o banco de dados funcione instalar db_browser
https://sqlitebrowser.org/dl/

"""
#dimensão do objeto janela
janela = ctk.CTk()

#define o inicio de todo comando
class Application():
    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()


    #aparencia da janela
    def tema(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    #dimensão e definição da janela
    def tela(self):
        janela.geometry('700x350')
        janela.title('Sistema de Login')
        janela.iconbitmap('icon.ico')
        janela.resizable(False, False)

    #imagem da tela
    def tela_login(self):
        img = PhotoImage(file='log.png')
        label_img = ctk.CTkLabel(master=janela, image=img, text='').place(x=45, y=60)

        #titulo acima do logo
        titulo_1 = ctk.CTkLabel(master=janela, text='Plataforma Python', font=('Roboto', 18, 'bold'), text_color='#FFFFFF').place(x=100, y=30)

        #frames tela de login a direira
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        #frame widgets
        #label texto acima do login
        titulo_2 = ctk.CTkLabel(master=login_frame, text='Faça o Login Para Acessar', font = ('Roboto', 20), text_color= ('white')).place(x=60, y=30)

        #campo de preenchimento usuário
        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text='Usuário', width=300, font=('Roboto', 15)).place(x=25, y=95)

        #campo de preenchimento senha
        campo_senha = ctk.CTkEntry(master=login_frame, placeholder_text='Senha', width=300, font=('Roboto', 15), show='*').place(x=25, y=140)

        #texto abaixo  do campo senha obrigatorio
        sub_titulo = ctk.CTkLabel(master = login_frame, text='TODOS OS CAMPOS SÃO OBRIGATÓRIOS*', font=('Roboto', 8), text_color= ('white')).place(x=168, y=170)

        
        #caixa para salvar login
        checkbox = ctk.CTkCheckBox(master = login_frame, text='Lembrar Senha').place(x=25, y=200)

        def login():
            msg = messagebox.showinfo(title= 'Status do Login', message='Login executado com sucesso!')
            
        #botão Login com comando messagebox acima
        btn_login = ctk.CTkButton(master=login_frame, text='LOGIN', width=300, command=login).place(x=25, y=240)

        #texto cadastre-se
        register_span = ctk.CTkLabel(master=login_frame, text='Criar uma conta para acessar.').place(x=25, y=285)

        #Esta Classe gera comando para chamar tela para registro
        def tela_registro():
            #remove a tela de login
            login_frame.pack_forget()

            #Tela de registro cadastro de usuários
            rg_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            rg_frame.pack(side=RIGHT)

            #Título Cadastre-se
            titulo_2 = ctk.CTkLabel(master=rg_frame, text='Cadastre-se', font = ('Roboto', 20), text_color= ('white')).place(x=120, y=30)

            #texto campo senha obrigatorio
            sub_titulo = ctk.CTkLabel(master = rg_frame, text='TODOS OS CAMPOS SÃO OBRIGATÓRIOS*', font=('Roboto', 8), text_color= ('white')).place(x=168, y=220)

            #campo de preenchimento nome do usuário
            username_entry = ctk.CTkEntry(master=rg_frame, placeholder_text='Nome', width=300, font=('Roboto', 15)).place(x=25, y=75)

            #campo de preenchimento e-mail do usuário
            email_entry = ctk.CTkEntry(master=rg_frame, placeholder_text='E-mail', width=300, font=('Roboto', 15)).place(x=25, y=115)

            #campo de preenchimento Senha usuário
            senha_entry = ctk.CTkEntry(master=rg_frame, placeholder_text='Senha', width=300, font=('Roboto', 15), show='*').place(x=25, y=155)

            #campo de preenchimento Confirmação de senha usuário
            cSenha_entry = ctk.CTkEntry(master=rg_frame, placeholder_text='Repita a Senha', width=300, font=('Roboto', 15), show='*').place(x=25, y=195)
       
            #caixa para aceite dos termos
            checkbox = ctk.CTkCheckBox(master = rg_frame, text='Aceito os termos de uso.').place(x=25, y=245)

            def back():
                #apaga a tela atual e volta a anterior
                rg_frame.pack_forget()
                login_frame.pack(side=RIGHT)

            #botão voltar com comando back
            btn_voltar = ctk.CTkButton(master=rg_frame, text='VOLTAR', width=135, fg_color='gray', hover_color='#696969', command=back).place(x=25, y=285)

            #definindo o botao comando salvar usuario
            def salvar_usuario():
                msg = messagebox.showinfo(title='Status do Cadastro', message='Usuário cadastrado com sucesso!')
                
            #botão registro
            btn_registro = ctk.CTkButton(master=rg_frame, text='SALVAR', width=135, fg_color='green', hover_color='#006400', command=salvar_usuario).place(x=190, y=285)

            

#botão registro
        btn_cadastro = ctk.CTkButton(master=login_frame, text='CADASTRE-SE', width=100, fg_color='green', hover_color='#006400', command=tela_registro).place(x=225, y=285)

Application()


