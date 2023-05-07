""" 
Bloque: Vista segunda pantalla
"""
import tkinter as tk
import customtkinter
from controladores import Controlador

class Frame_2(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        # instansia
        self.controlador = Controlador("Humano")
        #----------------------- Variables locales-------------------------
        # dimenciones de pantalla
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight() - 250

        self.widthFrames = 450
        self.border_color = 'gray27'



        #----------------- Custon frame principal ------------------------
        frame = customtkinter.CTkFrame(master=self, 
                                       corner_radius=0)
        frame.pack(expand=True)
        frame.grid(pady=15, padx=10)

        # --------------------- text area --------------------------
        frameTextArea = customtkinter.CTkTextbox(master=frame, 
                                               border_width=1,
                                               border_color=self.border_color, 
                                               width=self.widthFrames, height=self.height, 
                                               corner_radius=5)
        frameTextArea.grid(column=0, row=0, pady=(0,6))
        frameTextArea.grid_rowconfigure(0, weight=1)
        frameTextArea.grid_columnconfigure(0, weight=1)
        
        #--------------------- input area ----------------------
        frameInput = customtkinter.CTkEntry(master=frame, 
                                                    border_width=1,
                                                    border_color=self.border_color, 
                                                    width=self.widthFrames, height=40, 
                                                    corner_radius=5,
                                                    placeholder_text="Ingrese su mensaje")
        frameInput.grid(column=0, row=1, pady=(0,6))
        
        button = customtkinter.CTkButton(master=frame,
                                         text="Enviar",
                                         command= lambda:self.controlador.send(frameInput,frameTextArea))
        button.grid(column=0, row=2, pady=(0,6))
        