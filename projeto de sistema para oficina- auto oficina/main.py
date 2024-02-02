import customtkinter as ctk
from tkinter import *
from PIL import Image

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
        janela.geometry("950x500")
        janela.title("Auto Oficina")
        janela.iconbitmap("engrenagem.ico")
        janela.resizable(False, False)

    def tela_login(self):
        #trabalhando com a imagem
        img = ctk.CTkImage(Image.open("off.png"),size=(510,300))
        label_img = ctk.CTkLabel(master=janela, image=img, text="")
        label_img.place(x=5, y=65)

        label_title = ctk.CTkLabel(master= janela, text= "O sistema ideal para a sua Oficina", font=("Roboto", 25), text_color= "white"). place(x=100, y=10)

        #login_frame
        login_frame = ctk.CTkFrame(master=janela, width=400, height=500)
        login_frame.pack(side=RIGHT)

        #login_frame widgets
        title_label = ctk.CTkLabel(master=login_frame, text="Auto Oficina - Login",  text_color="red", font=("Roboto", 25))
        title_label.place(x=100, y=20)

        username = ctk.CTkEntry(master=login_frame, placeholder_text="Nome do usuario", font=("Roboto", 15),width=350, height=40). place(x=25, y=95)
        label_username = ctk.CTkLabel(master=login_frame, text=" * O campo nome de usuario e obrigatorio", text_color="red", font=("Roboto", 13)). place(x=25 , y=135)

        senha = ctk.CTkEntry(master=login_frame, placeholder_text="Senha do usuario", font=("Roboto", 15),width=350, height=40, show="*"). place(x=25, y=165)
        label_senha = ctk.CTkLabel(master=login_frame, text=" * O campo senha de usuario e obrigatorio", text_color="red", font=("Roboto", 13)). place(x=25 , y=205)

        checkbox = ctk.CTkCheckBox(master=login_frame, text="Manter - me conectado"). place(x=25, y=245)

        btn_login = ctk.CTkButton(master=login_frame, text = "Entrar", width=350,height=40, fg_color="red",hover_color="#FF6347"). place(x=25, y=295)
        
        def tela_cadastrar():
            #Remover o frame de login
            login_frame.pack_forget()
            
            #Tela de Cadastro 
            cadastro_frame = ctk.CTkFrame(master=janela, width=400, height=500)
            cadastro_frame.pack(side=RIGHT) 
            
            title_label = ctk.CTkLabel(master=cadastro_frame, text="Auto Oficina - Cadastro",  text_color="red", font=("Roboto", 25))
            title_label.place(x=80, y=20)

            username = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Nome do usuario", font=("Roboto", 15),width=350, height=40). place(x=25, y=95)
            label_username = ctk.CTkLabel(master=cadastro_frame, text=" * O campo nome de usuario e obrigatorio", text_color="red", font=("Roboto", 13)). place(x=25 , y=135)

            senha = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Senha do usuario", font=("Roboto", 15),width=350, height=40, show="*"). place(x=25, y=165)
            label_senha = ctk.CTkLabel(master=cadastro_frame, text=" * O campo senha de usuario e obrigatorio", text_color="red", font=("Roboto", 13)). place(x=25 , y=205)         
            pass
        cadastrar_mensagem = ctk.CTkLabel(master=login_frame, text="Não tem uma conta?  ").place(x=25, y=365)
        btn_cadastrar = ctk.CTkButton(master=login_frame, text="Cadastrar", width=200, height=35,fg_color="red",hover_color="#FF6347", text_color="white", command=tela_cadastrar).place(x=175, y=365)
Application()