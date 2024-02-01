import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("950x500")
janela.title("Auto Oficina")
janela.iconbitmap("engrenagem.ico")
janela.resizable(False, False)

#trabalhando com a imagem
img = PhotoImage(file="off.png")
label_img = customtkinter.CTkLabel(master=janela, image=img, text="")
label_img.place(x=5, y=65)

label_title = customtkinter.CTkLabel(master= janela, text= "O sistema ideal para a sua Oficina", font=("Roboto", 25),
                                     text_color= "white"). place(x=100, y=10)

#frame
frame = customtkinter.CTkFrame(master=janela, width=400, height=500)
frame.pack(side=RIGHT)

#frame widgets
label = customtkinter.CTkLabel(master=frame, text="Auto Oficina - Login",  text_color="red", font=("Roboto", 25))
label.place(x=100, y=20)

username = customtkinter.CTkEntry(master=frame, placeholder_text="Nome do usuario", font=("Roboto", 15),width=350, height=40). place(x=25, y=95)
label1 = customtkinter.CTkLabel(master=frame, text=" * O campo nome de usuario e obrigatorio", text_color="red", font=("Roboto", 13)). place(x=25 , y=135)

senha = customtkinter.CTkEntry(master=frame, placeholder_text="Senha do usuario", font=("Roboto", 15),width=350, height=40). place(x=25, y=165)
label2 = customtkinter.CTkLabel(master=frame, text=" * O campo senha de usuario e obrigatorio", text_color="red", font=("Roboto", 13)). place(x=25 , y=205)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Manter - me conectado"). place(x=25, y=245)

btn = customtkinter.CTkButton(master=frame, text = "Entrar", width=350,height=40). place(x=25, y=295)
janela.mainloop()