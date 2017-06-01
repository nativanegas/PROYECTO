from tkinter import *
import math, random, time




def mostrar(ventana): ventana.deiconify()
def ocultar(ventana):ventana.withdraw()

def ejecutar(f): Ventana_principal.after(200, f)
def salir(ventana):
    ventana.destroy()


Ventana_principal=Tk()
Ventana_principal.title("RoadFigther: Menú")
Ventana_principal.config(bg="blue")
Ventana_principal.geometry("500x500")
Ventana_principal.resizable(0,0)


LETRA1=("Ravie",10,"bold")
LETRA3=("Times New Roman",10,"bold")
LETRA4=("Times New Roman",15,"bold")

canvas_main=Canvas(Ventana_principal, width=500, height=500)
canvas_main.pack(fill='none')

######  FONDO
imagenf=PhotoImage(file="TITULO.gif")
fondo=Label(Ventana_principal,image=imagenf).place(x=0,y=0)
imagenfp=PhotoImage(file="FONDOPR.gif")
canvas_main.create_image(250, 280, image= imagenfp, anchor='center')

###### ENEMIGOS
imagenEne1 = PhotoImage(file="ENEMIGO.png")
imagenEne2 = PhotoImage(file="ENEMIGO2.png")
imagenEne3 = PhotoImage(file="ENEMIGO3.png")

imagenfp1=PhotoImage(file="pista1.gif") 
imagenfp2=PhotoImage(file="pista11.gif")   
filename = PhotoImage(file="coche1.png")
filename2 = PhotoImage(file="coche1.png")
filename3 = PhotoImage(file="coche2.png")
filename4 = PhotoImage(file="coche2.png")
fileGas = PhotoImage(file = "gas.png")
fileOil = PhotoImage(file = "oil.png")
fileboom = PhotoImage(file = "boom.png")
fileGO = PhotoImage(file = "game_over.png")


#-------BOTONES INICIALES---------------
B1=Button(Ventana_principal, text=" MANUAL ", font=LETRA1, command=lambda:ejecutar(salir(Ventana_principal)))
B1=Button(Ventana_principal, text=" MANUAL ", font=LETRA1, command=lambda:ejecutar(mostrar(manual_window)))
B2=Button(Ventana_principal, text="LOAD GAME",font=LETRA1, command=lambda:ejecutar(get_loaded_game()))
B3=Button(Ventana_principal, text="EXIT GAME",font=LETRA1, command=lambda: ejecutar(salir(Ventana_principal)))

B4=Button(Ventana_principal, text="LEVEL 1",font=LETRA3, command=lambda: ejecutar(mostrar(game_window)))

B5=Button(Ventana_principal, text="LEVEL 2",font=LETRA3, command=lambda: ejecutar(mostrar(game_window)))

B6=Button(Ventana_principal, text="LEVEL 3",font=LETRA3, command=lambda: ejecutar(mostrar(game_window)))


B7=Button(Ventana_principal, text="LEVEL 4",font=LETRA3, command=lambda: ejecutar(mostrar(game_window)))


B8=Button(Ventana_principal, text="LEVEL 5",font=LETRA3, command=lambda: ejecutar(show(game_window)))

B1.place(x=210,y=150)
B2.place(x=120,y=190)
B3.place(x=290,y=190)
B4.place(x=150,y=380)
B5.place(x=230,y=380)
B6.place(x=310,y=380)
B7.place(x=185,y=420)
B8.place(x=265,y=420)
#---------FIN BOTONES INICIALES-------------------

input_label= Label(Ventana_principal, text="PLAYER 1: ",font=LETRA3)
input_label.place(x=150, y=270)
nameP1 = StringVar()
nameP2 = StringVar()
speedJ1=0
speedJ2 = 0
gas1=100
gas2 = 100

entry_nameP1=Entry(Ventana_principal, textvariable= nameP1).place(x=230, y=270)
input_label2= Label(Ventana_principal, text="PLAYER 2: ",font=LETRA3)
input_label2.place(x=150, y=300)
entry_nameP2=Entry(Ventana_principal, textvariable= nameP2).place(x=230, y=300)

x = None
y = None
i=0
j=0
m=0
n=0


#################################################
##            VENTANA DEL MANUAL               ##
#################################################
manual_window = Toplevel(Ventana_principal)
manual_window.geometry("700x600")
manual_window.title("RoadFigther: MANUAL")
manual_window.config(bg="pink")
manual_window.resizable(0, 0)
b1_manual = Button(manual_window, text=" BACK TO MENU ", font=LETRA1, command=lambda: ejecutar(mostrar(Ventana_principal)))
b1_manual = Button(manual_window, text=" BACK TO MENU ", font=LETRA1, command=lambda: ejecutar(ocultar(manual_window)))
b1_manual.place(x=270, y=530)
Instr = Label(manual_window, text='ROADFIGHTER\n\n'
'INSTRUCCIONES:\n\n El juego consiste en la version original de road figther, desarrollado para dos jugadores \n'
'con distintas  carreteras; el objetivo es que el jugador debe llegar a cierta velocidad, siendo la velocidad \n'             
'en el primer nivel de 100, la cual va aumentando de 100 en 100 por nivel, es decir, que cuando uno de dos   \n'
'jugadores llegue a la velocidad dada en  el respectivo nivel, este ganará la partida   \n'

'El juega cuenta con 5 niveles distintos, en los cuales va aumentando la dificultad del juego \n'
'puesto que la velocidad de los enemigos es mayor. \n'

'De igual manera la gasolina de los carros disminuye cada cierta distancia, por lo cual a lo largo \n'
'de la pista  apareceran tanques de gasolina  con el fin de aumentar su nivel, pero a la vez \n'
'aparecerán manchas de aceite con el fin de desestabilizar el carro asi como carros enemigos \n'
'los cuales buscan chocarte.\n\n'

'CONTROLES:\n\n Ambos jugadores controlan su vehiculo con el teclado\n\n'
'< A > Para mover al Jugador 1 a la izquierda\n'
'< D > Para mover al Jugador 1 a la derecha\n'
'< J > Para mover al Jugador 2 a la izquierda\n'
'< L > Para mover al Jugador 2 a la derecha\n\n'
'CREDITOS:\n\n'
'Este juego fue creado puramente con el modulo Tkinter GUI para el lenguaje de programacion Python\n'
'por Natalia Vanegas Torres, estudiante de Matematicas Aplicadas para el curso\n'
'Introduccion a la Programacion en la Pontifica Universidad Javeriana, Cali, Colombia, 2017\n\n\n\n'
'\t\t\t\t¡Gracias por jugar!', fg='black', bg='pink', font=LETRA3, justify=LEFT)
Instr.pack()
################################################
##               VENTANA JUEGO                ##
################################################
game_window= Toplevel(Ventana_principal)



def level1():
    global game_window, Ventana_principal, canvas, p1_label, p2_label, nameP1, nameP2, entry_nameP1, entry_nameP2, name_player1, name_player2, speed_labelP1, speedP1, speed_labelP2, speedP2 
    global gas_labelP1, gasP1, gas_labelP2, gasP2, b1_game, b2_game, fondo1, imagenfp1, fondo2, imagenfp2, filename, filename2, filename3, filename4, speedJ1, speedJ2, gas1, gas2
    global enem1, enem11, enem22, enemigo_1, x1, y1,enem2, x2, y2, combust1, aceite1, fileGas, fileOil, posX1, posY1, posX2, posY2, carro1, carro2, fileboom, fileGO
    
    
    game_window.title("Road Fighter")
    game_window.resizable(0,0)
    #game_window.geometry("500x500")
    HEIGHT=465
    WIDTH=900

    canvas=Canvas(game_window, width=WIDTH, height=HEIGHT)
    canvas.pack(fill='none')

    #fondoprimernivel
    fondo1 = canvas.create_image(0,0, image=imagenfp1,anchor='nw')
    fondo2 = canvas.create_image(0,-465, image=imagenfp2,anchor='nw')

    #Enemigos  
    enem1 = canvas.create_image(100, -30,image=imagenEne1, anchor='center')
    enem2 = canvas.create_image(165, -10,image=imagenEne2, anchor='center')

    enem11= canvas.create_image(400, -30, image=imagenEne1, anchor='center')
    enem22 = canvas.create_image(465, -15,image=imagenEne2, anchor='center')
     
    #Aceite
    aceite1 = canvas.create_image(160, 200, image = fileOil, anchor= 'center')
    
    p1_label=Label(game_window,text="Player 1: ",font=LETRA1)
    p1_label.place(x=700 ,y=50)

    p2_label=Label(game_window,text="Player 2: ",font=LETRA1)
    p2_label.place(x=700 ,y=170)

    name_player1=Label(game_window, text="", font=LETRA1).place(x=790, y=52)
    name_player2=Label(game_window, text="", font = LETRA1).place(x=790, y=172)
    #----------------------------

    speed_labelP1=Label(game_window, text= "Speed:",font=LETRA4)
    speed_labelP1.place(x=700, y=80)

    speedP1=Label(game_window, text=  speedJ1)
    speedP1.place(x=765, y=85)

    gas_labelP1=Label(game_window, text="Gas:",font=LETRA4)
    gas_labelP1.place(x=700, y=110)

    #----------------------------
    speed_labelP2=Label(game_window, text= "Speed:",font=LETRA4)
    speed_labelP2.place(x=700, y=200)

    speedP2=Label(game_window, text= speedJ2)
    speedP2.place(x=765, y=205)

    gas_labelP2=Label(game_window, text="Gas:",font=LETRA4)
    gas_labelP2.place(x=700, y=230)

    #--------------------

    b1_game=Button(canvas, text="MENU",font=LETRA1, command=lambda: ejecutar(mostrar(Ventana_principal)))
    b1_game=Button(canvas, text="MENU",font=LETRA1, command=lambda: ejecutar(ocultar(game_window)))
    b2_game=Button(canvas, text="SAVE",font=LETRA1, command=lambda: get_arch_name())

    b1_game.place(x=780,y=280)
    b2_game.place(x=730,y=335)

    posX1=100
    posY1=400
    posX2=400
    posY2=400
    carro1 = canvas.create_image(posX1,posY1,image=filename)
    carro2 = canvas.create_image(posX2,posY2,image=filename3)

    game_window.iconify()
    game_window.bind_all()
    game_window.bind("<Key>", key)
    game_window.focus_set()

    mapa()
    enemigo_1()
    
    
    #gasolina()
    enemigo_2()
    manual_window.iconify()
    Ventana_principal.mainloop()

##############################
##      MOVIMIENTO          ##
##############################


def key(event):
    global carro1, carro2, i,j,m,n, canvas, posX1, posY1, posX2, posY2
    tecla = repr(event.char)
    #print(tecla)
    if(tecla == "'d'"):
        if(i < 85):
            canvas.delete(carro1)
            i = i + 10
            carro1 = canvas.create_image(posX1+i,posY1+j,image=filename)
            
                  
    if(tecla == "'a'"):
        if(i > -1):
            canvas.delete(carro1)
            i = i - 10
            carro1 = canvas.create_image(posX1+i,posY1+j,image=filename2)
        
    #---------------------------
    if(tecla == "'l'"):
        if(m < 85):
            canvas.delete(carro2)
            m = m + 10
            carro2 = canvas.create_image(posX2+m,posY2+n,image=filename3)
               
    if(tecla == "'j'"):
        if(m > -1):
            canvas.delete(carro2)
            m = m - 10
            carro2 = canvas.create_image(posX2+m,posY2+n,image=filename4)
    

def gasolina():
    global combust1
    combust1 = canvas.create_image(100, 200, image = fileGas, anchor= 'center')
    canvas.move(combust1, 0, 25)
    canvas.after(100, gasolina())

def aceite():
    global aceite1, createOil
    if canvas.coords(aceite1)[1] >= 470:
            canvas.delete(aceite1)
            canvas.after(100, createOil)
        
def mapa():
    global game_window, canvas, fondo1, fondo2, imagenfp1, imagenfp2, carro1, carro2, enem1, enem2, speedJ1, speedJ2, gas1, gas2, name_player1, name_player2, nameP1, nameP2
    global posX1, posY1, posX2, posY2, gas1, gas2, speedJ1, speedJ2, fileGO,speedJ1temporal,speedJ2temporal,gas1temporal,gas2temporal
    canvas.move(fondo1, 0, 0.8)
    canvas.move(fondo2, 0, 0.8)
    canvas.move(aceite1, 0, 0.8)
    if canvas.coords(fondo1)[1] >= 465 or canvas.coords(fondo2)[1] >= 465:
        canvas.delete(fondo1)
        fondo1 = canvas.create_image(0,0, image=imagenfp1,anchor='nw')
        canvas.delete(fondo2)
        fondo2 = canvas.create_image(0,-465, image=imagenfp2,anchor='nw')
        
        speedJ1 +=2
        speedJ1temporal=speedJ1
        speedJ2temporal=speedJ2
        gas1temportal=gas1
        gas2temporal=gas2
        speedJ2 +=2
        gas1 -=5
        gas2 -=5           
        
        speedP1=Label(game_window, text=  str(speedJ1), font = LETRA1).place(x=765, y=85)
        speedP2=Label(game_window, text= str(speedJ2), font = LETRA1).place(x=765, y=205)
        gasP1=Label(game_window, text=str(gas1), font = LETRA1).place(x=750, y=115)
        gasP2=Label(game_window, text=str(gas2), font = LETRA1).place(x=750, y=235)

        name_player1=Label(game_window, text=nameP1.get(), font=LETRA1).place(x=790, y=52)
        name_player2=Label(game_window, text=nameP2.get(), font = LETRA1).place(x=790, y=172)

                       
    canvas.after(10, mapa)

def kill():
    global Ventana_principal
    Ventana_principal.destroy()
def create():
    global canvas, enem1
    enem1= canvas.create_image(100, -30, image=imagenEne1, anchor='center')
def create2():
    global canvas, enem2
    enem2 = canvas.create_image(165, -15,image=imagenEne2, anchor='center')
    
def create11():
    global canvas, enem11
    enem11= canvas.create_image(400, -30, image=imagenEne1, anchor='center')
def create22():
    global canvas, enem22
    enem22 = canvas.create_image(465, -15,image=imagenEne2, anchor='center')

def createGas():
    global canvas, combust1
    combust1 = canvas.create_image(100, -10, image = fileGas, anchor= 'center')
def createOil():
    global canvas, aceite1
    aceite1 = canvas.create_image(160, -10, image = fileOil, anchor= 'center')

def enemigo_1():
    global game_window, canvas, enem1, enem2, carro1, carro2, fileboom, gas1, speedJ1, Ventana_principal
    x1, y1 = canvas.coords(enem1)
    x2, y2 = canvas.coords(enem2)
    canvas.after(1)
    canvas.move(enem1, 0, 0.3)
    canvas.after(1)
    canvas.move(enem2, 0, 0.6)
    if y1 >= 500 and y2 >= 500: 
        canvas.delete(enem1)
        canvas.after(10, create())
        canvas.delete(enem2)
        canvas.after(30, create2())
    if math.fabs(canvas.coords(carro1)[0] - canvas.coords(enem1)[0]) <= 30 and math.fabs(canvas.coords(carro1)[1] - canvas.coords(enem1)[1]) <= 61 or math.fabs(canvas.coords(carro1)[0] - canvas.coords(enem2)[0]) <= 30 and math.fabs(canvas.coords(carro1)[1] - canvas.coords(enem2)[1]) <= 61:
        canvas.itemconfig(carro1, image = fileboom)
        canvas.itemconfig(carro1, image = fileboom)
        gas1 -=10
        speedJ1 -= 2
        if (gas1 == 0 or gas1 <0) or (speedJ1==0 or speedJ1 < 0):
            canvas.create_image(200, 200, image = fileGO, anchor = 'center')
            #canvas.after(700, kill)
      
            
        
    canvas.move(enem1, 0, 1)
    canvas.move(enem2, 0, 2)
    game_window.after(20, enemigo_1)

def enemigo_3():
    global game_window, canvas, i, j
    x3, y3 = canvas.coords(enem3)
    canvas.after(1)
    canvas.move(enem3, 0, 0.3)
    if y4 >= 500 and y5 >= 500: 
        if(tecla == "'d'"):
            if(i < 85):
                i = i + 1
                canvas.move(enem3, pos1+i, 3)
        if(tecla == "'a'"):
            if(i > -1):
                i = i - 10
                canvas.move(enem3, pos1+i, 3)
    

def enemigo_2():
    global game_window, canvas, enem11, enem22, carro1, carro2
    x4, y4 = canvas.coords(enem11)
    x5, y5 = canvas.coords(enem22)
    canvas.after(1)
    canvas.move(enem11, 0, 0.3)
    canvas.after(1)
    canvas.move(enem22, 0, 0.6)
    if y4 >= 500 and y5 >= 500: 
        canvas.delete(enem11)
        canvas.after(10, create11())
        canvas.delete(enem22)
        canvas.after(30, create22())
    if math.fabs(canvas.coords(carro2)[0] - canvas.coords(enem11)[0]) <= 30 and math.fabs(canvas.coords(carro2)[1] - canvas.coords(enem11)[1]) <= 61 or math.fabs(canvas.coords(carro2)[0] - canvas.coords(enem22)[0]) <= 30 and math.fabs(canvas.coords(carro2)[1] - canvas.coords(enem22)[1]) <= 61:
        canvas.itemconfig(carro2, image = fileboom)
        canvas.itemconfig(carro2, image = fileboom)
        
    canvas.move(enem11, 0, 1)
    canvas.move(enem22, 0, 2)
    game_window.after(20, enemigo_2)
    

##############################
##    FIN VENTANA JUEGO     ##
##############################

# #------------------SAVE_GAME---------------------##
def get_arch_name():
    global arch_name
    arch_name = "Road_Fighter1"
    save_game()
    game_window.after(600, ejecutar(exit(Ventana_principal)))
def save_game():
    global speedJ1temporal, speedJ2temporal, gas1temporal, gas2temporal, name_player1, name_player2
    arch_def = arch_name
    saved_slot = open(arch_def+".txt", "w")
    pl_name = str(nameP1.get())
    points = str(speedJ1temporal)
    life = str(gas1temporal)
    pl2_name = str(nameP2.get())
    points2 = str(speedJ2temporal)
    life2 = str(gas2tmporal)
    saved_slot.write(pl_name + '\n')
    saved_slot.write(points + '\n')
    saved_slot.write(life + '\n')
    
    saved_slot.write(pl2_name + '\n')
    saved_slot.write(points2 + '\n')
    saved_slot.write(life2 + '\n')
    saved_slot.close()
# #------------------------------------------------##


# #------------------LOAD_GAME---------------------##
def get_loaded_game():
    load_game()
    main_window.after(500,ejecutar(mostrar(game_window)))
                      
def load_game():
    global speedJ1temporal, speedJ2temporal, gas1temporal, gas2temporal, nameP1, nameP2
    arch_def = "Road_Fighter1"
    saved_slot = open(arch_def+".txt", "r")
    nombre1 = saved_slot.readline()
    speedJ1temporal = saved_slot.readline()
    gas1temporal = saved_slot.readline()
    
    nombre2 = saved_slot.readline()
    speedJ2temporal = saved_slot.readline()
    gas2temporal = saved_slot.readline()
    
    name_player1.config(text=" " + nombre1)
    speedP1.config(text=" " + speedJ1temporal)
    gasP1.config(text=" " + gas1temporal)

    name_player2.config(text=" " + nombre2)
    speedP2.config(text=" " + speedJ2temporal)
    gasP2.config(text=" " + gas2temporal)
# #------------------------------------------------##

level1()


