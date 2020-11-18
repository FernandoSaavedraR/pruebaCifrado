from tkinter import Tk,Text, Button,Label, messagebox,StringVar,Menu
from sc import cifrar64,descifrar64
class Interfaz:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title('Cifrado')
               #agregar una caja de texto
        self.cadenaL = Label(ventana,text='Ingrese su cadena')
        self.cadena = Text(ventana, state="normal",width=40, height=3)
        self.Resultado = Label(ventana,text='El resultado es')
        self.cifrado = Text(ventana,state="disabled",width=40,height=3)
        self.cifrar = Button(ventana, activeforeground='green',text='cifrar',command = self.cifrarM)
        self.descifar = Button(ventana, activeforeground='green',text='descifrar',command = self.descifrarM)
        #ubicar la pantalla en la ventana
        self.cadenaL.grid(row=0,column=0,columnspan=2,padx=0,pady=1)
        self.cadena.grid(row=1,column=0,columnspan=2,padx=5,pady=0)
        self.cifrar.grid(row=2,column=0,padx=5,pady=5)
        self.descifar.grid(row=2,column=1,padx=5,pady=5)
        self.Resultado.grid(row=3,column=0,columnspan=2,padx=0,pady=5)
        self.cifrado.grid(row=4,column=0,columnspan=2,padx=5,pady=0)
    def cifrarM(self):
        cadena = self.cadena.get("1.0","end-1c")
        if(len(cadena.strip())<1):
            messagebox.showinfo(message='Ingrese una cadena',title='Cifrar')
        else:
            res = cifrar64(cadena)
            
            self.cifrado.configure(state="normal")
            self.cifrado.delete("1.0","end-1c")
            self.cifrado.insert('end-1c',res)
            self.cifrado.configure(state='disabled')

    def descifrarM(self):
        cadena = self.cifrado.get("1.0","end-1c")
        if(len(cadena.strip())<1):
            messagebox.showinfo(message='Cifre algo primero',title='descifrar')
        else:
            res = descifrar64(cadena)
            self.cadena.delete("1.0","end-1c")
            self.cadena.insert('end-1c',cadena)
            self.cifrado.configure(state="normal")
            self.cifrado.delete("1.0","end-1c")
            self.cifrado.insert('end-1c',res)
ventana_principal = Tk()
cifradora = Interfaz(ventana_principal)
ventana_principal.mainloop()