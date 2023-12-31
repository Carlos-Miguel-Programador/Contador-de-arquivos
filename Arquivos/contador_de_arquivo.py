import os
from tkinter import Listbox, messagebox
from ttkbootstrap import *

def Reiniciar(lista_arq, caminho, lb_rus, entry_caminho):
    lista_arq.delete(0, END)
    caminho.set('')
    lb_rus.set('')
    entry_caminho.focus()
    
def Contar(caminho, resultado, lista):
    path = caminho.get()
    
    if os.path.exists(path):
        lista_arq = os.listdir(path)
        item = 1
        
        if len(lista_arq) != 0:
            resultado.set('Arquivos encontrados: ' + str(len(lista_arq)))
            
            lista.delete(0, END)
            for arq in lista_arq:
                lista.insert(END, '[' + str(item) + ']' + ' - '+arq)
                item += 1
        else:
            resultado.set('Não há nenhum arquivo neste diretório')
    elif path == '':
        messagebox.showwarning('Atenção', 'O preenchimento do caminho é obrigatório')
        resultado.set('')
    else:
        lista.delete(0, END)
        resultado.set('Arquivos encontrados: 0')
        messagebox.showwarning('Atenção', 'Caminho não existe neste sistema')
        

# - JANELA PRICIPAL
janela = Window('Contador de arquivos')
janela.iconbitmap('IMG/logo-arq.ico')
janela.resizable(False, False)
Style('lumen')
janela.geometry('500x350+380+100')

# ! PRIMEIRA PARTE DA JANELA
label_frame1 = Labelframe(janela, text='Insira o caminho', borderwidth=2, width=470, height=100)
label_frame1.place(x=14, y=14)

caminho = StringVar()

entry_caminho = Entry(label_frame1, width=72, textvariable=caminho)
entry_caminho.bind('<Return>', lambda e: Contar(entry_caminho, lb_rus, lista_de_arquivos))
entry_caminho.focus()
entry_caminho.place(x=10, y=10)

botao_procurar = Button(label_frame1, text='Contar', width=15, command=lambda: Contar(entry_caminho, lb_rus, lista_de_arquivos))
botao_procurar.place(x=130, y=50)

img = PhotoImage('reiniciar.png')

botao_reiniciar = Button(label_frame1, text='Reiniciar', bootstyle=DANGER, command=lambda: Reiniciar(lista_de_arquivos, caminho, lb_rus, entry_caminho))
botao_reiniciar.place(x=260, y=50)
# ! PRIMEIRA PARTE DA JANELA

# * SEGUNDA PARTE DA JANELA
label_frame2 = Labelframe(janela, text='Resultado', borderwidth=2, width=470, height=222)
label_frame2.place(x=14, y=115)

lb_rus = StringVar()

label_resultado = Label(label_frame2, font=('Arial', 11), textvariable=lb_rus)
label_resultado.place(x=10, y=0)

lista_de_arquivos = Listbox(label_frame2, width=int(63.5), height=9, font=('Arial', 10))
lista_de_arquivos.place(x=10, y=30)
# * SEGUNDA PARTE DA JANELA

janela.mainloop()
# - JANELA PRICIPAL