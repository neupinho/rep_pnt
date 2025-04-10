import tkinter as tk
from tkinter import messagebox
from pygame import mixer
import threading
import time
from PIL import Image, ImageTk

#bandeira
executando = False  

def iniciar_alarme(intervalo):
    global executando
    try:
        #pra seg
        tempo_espera = float(intervalo) * 60
        executando = True
        messagebox.showinfo("Alarme", "O tempo para bebeção de água foi iniciado!") 
        
        def executar_alarme():
            while executando:
                time.sleep(tempo_espera)
                if executando: 
                    #som usando pygame
                    mixer.init()
                    mixer.music.load("bebecao.mp3")
                    mixer.music.play()
                    messagebox.showinfo("es hora de beber agua", "es hora de beber agua")
        
        #thread
        threading.Thread(target=executar_alarme, daemon=True).start()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido!")

def cancelar_alarme():
    global executando
    if executando:
        executando = False 
        mixer.music.stop()
        messagebox.showinfo("Alarme", "O alarme foi cancelado!")
    else:
        messagebox.showwarning("Alarme", "Nenhum alarme está ativo.")


janela = tk.Tk()
janela.title("Alarme de Beber Água")
rotulo = tk.Label(janela, text="De quanto em quanto tempo você quer beber água? (minutos):", font=("Calibri", 12))
rotulo.pack(pady=10)


imagem = Image.open("garrafa.jpg")
imagem_redimensionada = imagem.resize((100, 150)) 
imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
rotulo_imagem = tk.Label(janela, image=imagem_tk)
rotulo_imagem.pack()

entrada_tempo = tk.Entry(janela)
entrada_tempo.pack()

botao_iniciar = tk.Button(janela, text="Iniciar Alarme", command=lambda: iniciar_alarme(entrada_tempo.get()))
botao_iniciar.pack()
botao_cancelar = tk.Button(janela, text="Cancelar Alarme", command=cancelar_alarme)
botao_cancelar.pack()

janela.mainloop()
