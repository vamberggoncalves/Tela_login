import customtkinter as ctk
from tkinter import*
from tkinter import messagebox

janela = ctk.CTk()
class Application():
    
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()
        

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de Login")
        janela.resizable(False,False)

    def tela_login(self):

        #label e imagens
        texto = ctk.CTkLabel(janela,text="Seja \n bem - Vindo !!!!",font=("Roboto",50),text_color="#00B0F0")
        texto.place(x=10,y=85)
        #frame
        login_frame = ctk.CTkFrame(janela,width=350,height=400)
        login_frame.pack(side=RIGHT)

        #frame widgets
        label_logo = ctk.CTkLabel(login_frame,text="Sistema de Login",font=("Roboto",28),text_color="#00B0F0")
        label_logo.place(x=70,y=35)
        

        usuario = ctk.CTkEntry(login_frame,placeholder_text="Nome do usuario",font=("roboto",20),width=300)
        usuario.place(x=25,y=105)

        usuario_label = ctk.CTkLabel(login_frame,text="*campo Usuario obrigario",text_color="green",font=("Roboto",10))
        usuario_label.place(x=25,y=135)

        password1 = ctk.CTkEntry(login_frame,placeholder_text="Senha Usuario",font=("roboto",20),width=300)
        password1.place(x=25,y=175)

        password_label = ctk.CTkLabel(login_frame,text="*campo Senha Obrigario",text_color="green",font=("Roboto",10))
        password_label.place(x=25,y=205)

        chekbox = ctk.CTkCheckBox(login_frame, text="Marter-me conectado")
        chekbox.place(x=25,y=235)

        butao = ctk.CTkButton(login_frame,text="LOGIN",width=300)
        butao.place(x=25,y=285)

        def tela_cadastrar():
            #removendo widgets
            login_frame.pack_forget()

            #criando frame do cadastrar
            cadastro_frame = ctk.CTkFrame(janela,width=350,height=396)
            cadastro_frame.pack(side = RIGHT)

            #criando os label
            label_cadastro = ctk.CTkLabel(cadastro_frame, text="Crie a sua Conta",font=("Roboto",22))
            label_cadastro.place(x=25,y=5)
            label_informativo = ctk.CTkLabel(cadastro_frame,text="* Preencha todos os campos com dados corretos \n são de extrema importância para a nossa plataforma!",font=("Roboto",12))
            label_informativo.place(x=28,y=45)

            #criando os entry
            user_name = ctk.CTkEntry(cadastro_frame,placeholder_text="Nome do usuario",font=("roboto",20),width=300)
            user_name.place(x=25,y=105)

            emai_user = ctk.CTkEntry(cadastro_frame,placeholder_text="Seu E-mail",font=("Roboto",20),width=300)
            emai_user.place(x=25,y=145)

            senha_user = ctk.CTkEntry(cadastro_frame,placeholder_text="Senha do Usuario",font=("Roboto",20),width=300)
            senha_user.place(x=25,y=185)

            confirm_senha = ctk.CTkEntry(cadastro_frame,placeholder_text="Confirme a Senha",font=("Roboto",20),width=300)
            confirm_senha.place(x=25,y=225)

            chekbox_cadastro = ctk.CTkCheckBox(cadastro_frame,text="Aceito todos Termos Politicas",font=("Roboto",12))
            chekbox_cadastro.place(x=25,y=265)

            def back():
                #removendo o frame de cadastro
                cadastro_frame.pack_forget()

                #devolvendo tela de login
                login_frame.pack(side=RIGHT)

                
            botao_voltar = ctk.CTkButton(cadastro_frame,text="VOLTAR",width=145,fg_color="gray",hover_color="#202020",command=back)
            botao_voltar.place(x=25,y=315)

            def cadastrado():
                cadastrado = ctk.CTkLabel(messagebox.showinfo(title="Status cadastrado",message="cadastrado com sucesso"))
                

            botao_castrando = ctk.CTkButton(cadastro_frame,text="CADASTRAR",width=145,fg_color="green",hover_color="#014B05",command=cadastrado)
            botao_castrando.place(x=180,y=315)

        #label e botao da tela de login   
        cadastre_label = ctk.CTkLabel(login_frame,text="Criar conta -->",font=("Roboto",20),text_color="green")
        cadastre_label.place(x=25,y=325)

        botao_cadastrar = ctk.CTkButton(login_frame,text="Cadastrar Conta",fg_color="green",hover_color="#2D9334",width=150,command=tela_cadastrar)
        botao_cadastrar.place(x=175,y=325)

Application()

