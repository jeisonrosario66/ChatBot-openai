import tkinter as tk
import customtkinter
from vistas.frame2 import Frame_2


class Frame_1(tk.Frame):
    def __init__(self, container, controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)

        width= self.winfo_screenwidth()
        height= self.winfo_screenheight()

        frame = customtkinter.CTkFrame(master=self, corner_radius=0)
        frame.pack(expand=True)

        userName = customtkinter.CTkLabel(master=frame, text='Ingrese su nombre')
        userName.grid(column=1, row=0, pady=10)
        
        input = customtkinter.CTkEntry(master=frame,
                                       width=220)
        input.grid(column=1,row=1, padx=10, pady=(0,10))

        button = customtkinter.CTkButton(master=frame, width=50, height=32, corner_radius=8, text="Ingresar al Bot", command= lambda:controller.show_frame( Frame_2 ))
        button.grid(column=1,row=2, sticky = "nsew", pady=(0,10))

    
