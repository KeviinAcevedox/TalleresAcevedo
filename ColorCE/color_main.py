# Importar los módulos que se van a usar en el juego
from tkinter import *
import random
from playsound import playsound
from db import *

# lista de colores que se van a usar para las palabras
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']

# Variable que guarda el puntaje del usuario en las partidas
score = 0

# Variable que guarda el tiempo restante para que acabe la partida
timeleft = 60

# Se lee el score que está en la base de datos y se almacena en una variable
top_score = get_score('user_score.txt')

#***********************************************************************************************************************
# Función que se llama cada vez que se presione la tecla <Enter>
def startGame(event):

    # La variabñe timeleft es igual a 60 cuando recién empieza una partida
    if timeleft == 60:
        # Primero se modifica el texto del label que muestra el contador
        timeLabel.config( text = "Time left: " + str(timeleft), bg='SkyBlue1', font = ('Helvetica', 28))
        # Se actualiza el score en la pantalla
        scoreLabel.config(text = "Score: " + str(score))
        playsound('lets go.mp3', block=False)

        countdown()

    # Cada vez que se presione la tecla <Enter> se debe cambiar de palabra y color
    nextColour()

#***********************************************************************************************************************
# Función que valida lo que el usuario escribe en el entry y cambia de palabra y color
def nextColour():
    global score, timeleft

    # Mientras la partida esté activa
    if timeleft > 0:
        # Se concentra en el entry
        e.focus_set()

        # Comparación de la palabra escrita por el usuario y el color de la palabra mostrada en pantalla
        # Si coinciden, se debe reproducir un sonido de success y aumentar el score
        if e.get().lower() == colours[1].lower():
            playsound('success.mp3', block=False)
            score += 1
            # Se actualiza el score en la pantalla
            scoreLabel.config(text = "Score: " + str(score))
            # Se analiza el puntaje de la partida realizada
            set_score(score)

        # Si no coincide, se reproduce un sonido de error
        elif e.get().lower() != colours[1].lower() and e.get().lower() != '':
            playsound('error.mp3', block=False)


        # Sin importar el resultado, se vacía el entry
        e.delete(0, END)

        # Se revuelven las palabras en el array
        random.shuffle(colours)

        # Se configura la nueva palabra y el color de la palabra
        word.config(fg = str(colours[1]), text = str(colours[0]))

#***********************************************************************************************************************
def countdown():
    global timeleft, score

    # Mientras la partida esté activa
    if timeleft > 0:
        timeleft -= 1

        # Se actualiza el label del tiempo
        timeLabel.config(text = "Time left: " + str(timeleft))

        timeLabel.after(1000, countdown)

    # Si la partida ya terminó
    else:
        # Se reproduce un sonido prara indicar que ya acabó la partida
        playsound('finish.mp3', block=False)
        # Se quita el texto del score y se cambia por un mensaje de inicio de partida
        scoreLabel.config(text = "Press enter to start")
        # Se ocultan los labels del tiempo y la palabra en la pantalla
        timeLabel.config(text='')
        word.config(text='')
        # Se resetean las variables del tiempo restante y el score
        timeleft = 60
        score = 0
        # Se vacía el entry
        e.delete(0, END)
        # Se posiciona al usuario en el entry
        e.focus_set()

#***********************************************************************************************************************
# Función que verifica si el usuario ha superado el record
# En caso de que sea verdadero, se reproduce un sonido de victoria y luego se actualiza el nuevo puntaje en la db
def set_score(new_score):
    global top_score

    # Se verifica si el puntaje que acaba de hacer el usuario ha superado el máximo alcanzado
    if new_score > get_score('user_score.txt'):
        playsound('max_score.mp3', block=False)
        update_score('user_score.txt', new_score)
        top_score = new_score
        # Se actualiza el nuevo top score en la pantalla
        top_score_label.config(text= 'Top Score: ' + str(top_score))

#***********************************************************************************************************************
# Se define la raiz principal del juego
root = Tk()

# se define el título de la ventana
root.title("COLOR GAME")

# Obtener el ancho y alto de la pantalla de la computadora
height = root.winfo_screenheight()
width = root.winfo_screenwidth()

# Se define el tamaño de la ventana acorde con las dimensiones del dispositivo
root.geometry(str(width) + 'x' + str(height))

# Se le coloca un fondo gris a la ventana
root.configure(bg='SkyBlue1')

top_score_label = Label(root, text= 'Top Score: ' + str(top_score) , bg='SkyBlue1', fg='yellow', font = ('Helvetica', 20))
top_score_label.pack(pady=10)

# Se escribe un título en la pantalla de la ventana principal
title = Label(root, text='Color Game', bg='SkyBlue1', fg='green', font = ('Rosewood Std Regular', 60))
title.pack(side=TOP, pady=50)

# Se añade un Label con las instrucciones del juego
instructions = Label(root, text = "Escribe el color, no la palabra!", bg='SkyBlue1', font = ('Helvetica', 28))
instructions.pack(side=TOP, pady=10)

# Se define un Label para mostrar el score que tiene el usuario
# Pero antes se usa para mostrar indicaciones de cómo emprezar la partida
scoreLabel = Label(root, text = "Press enter to start", bg='SkyBlue1', fg='white', font = ('Helvetica', 28))
scoreLabel.pack(side=TOP, pady=20)

# Se define un Label para mostrar el tiempo restante
# Es vacío antes de que inicie la partida
timeLabel = Label(root, bg='SkyBlue1')

timeLabel.pack(side=TOP, pady=30)

# Se define un Label para mostrar la palabra con un color
# Es vacío antes de que inicie la partida
word = Label(root, bg='SkyBlue1', font = ('Helvetica', 60))
word.pack(side=TOP, pady=20)

# Se añade un Widget de tipo Entry para que el usuario pueda escribir los colores
e = Entry(root, font = ('Helvetica', 18))

# Le indicamos a la raiz que se debe ejecutar la función <startGame> cuando el usuario presione la tecla Enter
root.bind('<Return>', startGame)
e.pack(ipady=10, side=TOP, pady=20)

# Se posiciona al usuario en el Widget Entry
e.focus_set()

# Se inicia la interfaz gráfica de usuario
root.mainloop()