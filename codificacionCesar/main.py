from tkinter import *
from tkinter import messagebox
from modulos.archiva import *
from modulos.cesar import *

def codificar():
    texto =textoSincodificar.get()
    textoCodificado.set(codifica(texto))

def descodificar():
    texto=textoCodificado.get()
    if texto !="":
        textoSincodificar.set(descodifica(texto))
        mensaje("info","texto descodificado")
    else:
        mensaje("error","error al descodificar el texto")

def cargar():
    try:
        textoCodificado.set(carga())
        descodificar()
    except:
        mensaje("error","error al cargar el archivo")

def guardar():
    texto = textoCodificado.get()
    if texto != "":
        guarda(texto)
        mensaje("info","mensaje guardado")
    else:
        mensaje("error","error al guardar")

def borrar():
    textoCodificado.set()
    textoSincodificar.set()
def mensaje(titulo,texo):
    messagebox.showinfo(titulo,texo)

def mensaje(titulo,texto):
    messagebox.showinfo(titulo,texto)






ventana =Tk()
ventana.title("codifica")
ventana.config(bg="gray")
ventana.geometry("380x380")
frame=Frame()
frame.config(width=340,height=340)
frame.config(bg="cyan")
frame.pack()
textoSincodificar= StringVar()
textoCodificado=StringVar()
etiquetaSincodificar=Label(frame,text="texto sin codificar").grid(row=3,column=1)
cajaSin =Entry(frame,textvariable=textoSincodificar).grid(row=3,column=2)

etiquetacodificar=Label(frame,text="texto codificado").grid(row=4,column=1)
cajacodificada =Entry(frame,textvariable=textoCodificado).grid(row=4,column=2)

botonCodificar=Button(frame,text="codificar",command=codificar).grid(row=5,column=1)
botondescodificar=Button(frame,text="descodificar",command=descodificar).grid(row=5,column=2)
botongrabar=Button(frame,text="grabar",command=guardar).grid(row=6,column=1)
botoncargar=Button(frame,text="cargar",command=cargar).grid(row=6,column=2)
botonborrar=Button(frame,text="borrar",command=borrar).grid(row=7,column=1)













ventana.mainloop()