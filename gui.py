from tkinter import *
from main import BotChat

# GUI
root = Tk()
root.title("Chat Bot - Reto 4")

# Constantes de estilos
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():

    # Instancia del objeto bot
    bot = BotChat("jeison")
	
	# send = nombre del usuario + campo de entrada de usuario.obtener
    send = f"{bot.userName}: " + inputUser.get()
    
    # txt.insertar al area de texto(espacio + mensaje enviado al bot)
    txt.insert(END, "\n" + send)
    
    # bot.metodo(texto introducido por el usuario.obtener)
    bot.pregunta(inputUser.get().strip())
    
    # txt.insertar al area de texto(espacio + respuesta del bot)
    txt.insert(END, "\n" + bot.respuestaTxt)
    
    # Limpia el campo de input
    inputUser.delete(0, END)

lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Chat Bot - Etapa 1", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

# label area de texto mas grande
txt = Text(root, bg="RED", fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

# label barra de desplasamiento vertical
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

#label input de usuario
inputUser = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
inputUser.grid(row=2, column=0)

# boton send para enviar la data introducida
send = Button(root, text="Enviar", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()