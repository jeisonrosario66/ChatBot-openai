""" 
Bloque: Vista principal
"""
#---------------- Ventanas HD (Si es posible) -------------------
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

import tkinter as tk
import customtkinter
from tkinter import messagebox, Menu
from frame1 import Frame_1
from frame2 import Frame_2


#  ------------Custon Tkinter (apariencia)-------------------
customtkinter.set_appearance_mode("system")  # default value
#customtkinter.set_appearance_mode("dark")
#customtkinter.set_appearance_mode("light")

#customtkinter.set_default_color_theme("blue")
customtkinter.set_default_color_theme("dark-blue")
#customtkinter.set_default_color_theme("sweetkind")
#customtkinter.set_default_color_theme("green")

#-------------------Clase Principal -----------------------------
class APP(tk.Tk):
    def __init__(self,*args,**kwargs):
        #Se inicializa ademas, con la herencia de tk.Tk, para tener todas estas disponibilidades en "self"
        super().__init__(*args,**kwargs)

        #--------------------- Configuracion ventana principal ------------------#
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        #self.geometry("%dx%d" % (width, height-100))
        #self.minsize(width-100, height-100)
        self.title("ChatBot - Reto 4 DigitalNao")
        #self.iconbitmap('') # Icono de app

        #---------------- Contruccion Barra Menu ------------
        self.menuBarra = Menu(self) # Declaracion de la barra menu
        self.configure(menu = self.menuBarra)

            #----- Elementos Barra Menu -----
        # menuArchivo = Menu(self.menuBarra, tearoff=0)
        # menuArchivo.add_command(label='Abrir archivo...')
        # menuArchivo.add_command(label='Nuevo archivo...')
        # menuArchivo.add_command(label='Guardar Archivo')
        # menuArchivo.add_separator()
        # menuArchivo.add_command(label='Cerrar')
        # menuArchivo.add_command(label='Salir')

        menuAyuda = Menu(self.menuBarra, tearoff=0)
        menuAyuda.add_command(label='Documentacion', command=lambda:self.aviso())
        menuAyuda.add_command(label='Acerca de...', command=lambda:self.avisoInfo())

            #----- Renderizado -----
        # self.menuBarra.add_cascade(label='Archivo', menu=menuArchivo) 
        self.menuBarra.add_cascade(label='Ayuda', menu=menuAyuda) 
        
        #Se busca que Ventana se mantenga central y correcta independiente del tamanno y expansiones realizadas:
        self.columnconfigure( 0, weight = 1 )
        self.rowconfigure(0, weight = 1)

        contenedor_principal = tk.Frame( self )
        contenedor_principal.grid(sticky = "nsew")

        # Diccionario contiene todos los Frames
        self.todos_los_frames = dict()

        # Recorre tupla con los frames para ser llamados al contenedor principal
        for F in (Frame_1, Frame_2):
            frame = F( contenedor_principal , self)
            self.todos_los_frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame( Frame_1 )

    def aviso(self): # ventana emerjente de aviso
        messagebox.showinfo('Procesador de planillas','Funcionalidad Pendiente de implementar...\n!!!!!!!!!!!!!!!!!!!!!!!!')

    def avisoInfo(self): # ventana emerjente de aviso
        messagebox.showinfo('Procesador de planillas','Desarrollado por: Jeison Rosario.\nContacto: jeisonrosario5@gmail.com')

    #METODO PARA MOSTRAR UNICAMENTE FRAME DESEADO (controller = Clase que queremos obtener de diccionario de frames)
    def show_frame(self,contenedor_llamado):
        frame = self.todos_los_frames[contenedor_llamado]
        frame.tkraise()

root = APP()
root.mainloop()