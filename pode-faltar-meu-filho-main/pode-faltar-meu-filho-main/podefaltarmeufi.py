import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame

def carregar_imagem(caminho, tamanho=(200, 200)):
    try:
        imagem = Image.open(caminho)
        imagem = imagem.resize(tamanho, Image.LANCZOS)
        foto = ImageTk.PhotoImage(imagem)
        return foto
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        return None

def tocar_musica(caminho, start_pos=0.0):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(caminho)
    
    pygame.mixer.music.play(loops=0, start=start_pos)

def verificarfaltas():
    try:
        aulas = int(entrada.get())

        janela2 = tk.Toplevel()
        janela2.geometry("400x500")
        janela2.config(bg="lightblue")
        janela2.iconbitmap(r"c:/Users/aluno/Downloads/favicon.ico")

        if aulas > 300:
            janela2.title("Infelizmente...")
            foto = carregar_imagem(r"c:/Users/aluno/Downloads/Arquivos/jesus triste.png")
            if foto:
                label_imagem = tk.Label(janela2, image=foto, bg="lightblue")
                label_imagem.image = foto
                label_imagem.pack(pady=10)
            else:
                tk.Label(janela2, text="Imagem não encontrada", fg="red", bg="lightblue").pack(pady=10)

            texto = ("Infelizmente... aproveitou desmasiadamente\n"
                     "e decidiu faltar muito...você ja repetiu de ano")
            label2 = tk.Label(janela2, text=texto, bg="lightblue", justify="center")
            label2.pack(pady=20)
            tocar_musica(r"C:/Users/aluno/Downloads/Arquivos/Nutshell_M4A_128K_.mp3")

        elif 250 <= aulas <= 300:
            janela2.title("Cuidado...")
            foto = carregar_imagem(r"C:/Users/aluno/Downloads/Arquivos/jesus amigo de nós.jpg")
            if foto:
                label_imagem = tk.Label(janela2, image=foto, bg="lightblue")
                label_imagem.image = foto
                label_imagem.pack(pady=10)
            else:
                tk.Label(janela2, text="Imagem não encontrada", fg="red", bg="lightblue").pack(pady=10)

            texto = ("Então...\nmeu filho deve tomar cuidado, pois o terreno é sinuoso,\n"
                     "e a falta de presença é perigosa")
            label2 = tk.Label(janela2, text=texto, bg="lightblue", justify="center")
            label2.pack(pady=20)
            tocar_musica(r"C:/Users/aluno/Downloads/Arquivos/Musica-do-Toguro-Só-a-parte-certa_M4A_128K__1.mp3")

        else:
            janela2.title("Meu filho...")
            foto = carregar_imagem(r"c:/Users/aluno/Arquivos/Downloads/GLORY.jpg")
            if foto:
                label_imagem = tk.Label(janela2, image=foto, bg="lightblue")
                label_imagem.image = foto
                label_imagem.pack(pady=10)
            else:
                tk.Label(janela2, text="Imagem não encontrada", fg="red", bg="lightblue").pack(pady=10)

            texto = "Que orgulho, Está indo bem direitinho na escola... pode faltar meu filho"
            label2 = tk.Label(janela2, text=texto, bg="lightblue", justify="center")
            label2.pack(pady=20)
            # start=122.0 pode não funcionar em algumas versões pygame
            tocar_musica(r"C:/Users/aluno/Downloads/Arquivos/O-escudo-Voz-da-Verdade_M4A_128K__1.mp3", start_pos=122.0)

    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos meu filho ")

janela = tk.Tk()
janela.title("pode faltar meu filho")
janela.geometry("400x500")
janela.config(bg="lightblue")
janela.maxsize(400, 500)
janela.iconbitmap(r"c:/Users/aluno/Downloads/Arquivos/favicon.ico")

foto = carregar_imagem(r"C:/Users/aluno/Arquivos/Downloads/png.png")
if foto:
    label_imagem = tk.Label(janela, image=foto, bg="lightblue")
    label_imagem.image = foto
    label_imagem.pack(pady=10)
else:
    tk.Label(janela, text="Imagem não encontrada", fg="red", bg="lightblue").pack(pady=10)

label1 = tk.Label(
    janela,
    text="Olá meu filho\ncoloque seu número de faltas em número de aulas, por obséquio",
    justify="center",
    padx=20,
    pady=10,
    bg="lightblue"
)
label1.pack()

entrada = tk.Entry(janela, width=20, justify="center")
entrada.pack(pady=10)

botao = tk.Button(janela, text="verificar faltas", command=verificarfaltas, bg="#00008b", fg="white")
botao.pack(pady=10)

pygame.mixer.init()
pygame.mixer.music.load(r"C:/Users/aluno/Downloads/Arquivos/O-escudo-Voz-da-Verdade_M4A_128K__1.mp3")
pygame.mixer.music.play()

janela.mainloop()
