""" 
Bloque: controlador
"""
from tkinter import *
from bot_chat import BotChat

class Controlador():
    """Objeto encargado de conectar el modelo con la vista
    """
    def __init__(self,username):
        """Constructor instancia el objeto BotChat
        """
        # Instancia del objeto bot
        self.botchat = BotChat(username)
        
    def send(self, inputUser, textArea):
        """Meotodo cominica con el objeto BotChat

        Args:
            inputUser (CTkframe): Area donde el usuario introduce su consulta
            textArea (CTkframe): Area del registro del  dialogo entre usuario y bot
        """
        # send = nombre del usuario + campo de entrada de usuario.obtener
        send = f"{self.botchat.userName}: " + inputUser.get()
        
        # txt.insertar al area de texto(espacio + mensaje enviado al bot)
        textArea.insert(END, "\n" + send)
        
        # bot.metodo(texto introducido por el usuario.obtener)
        self.botchat.consulta(inputUser.get().strip())
        
        # txt.insertar al area de texto(espacio + respuesta del bot)
        textArea.insert(END, "\n" + self.botchat.respuestaTxt)
        
        # Limpia el campo de input
        inputUser.delete(0, END)
        
        