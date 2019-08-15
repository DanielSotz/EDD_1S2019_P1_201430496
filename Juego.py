

from ListaDoble import ListaDoble  
from Pila import PilaScore 

import random 
import curses 
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN 

global lista_serpiente
global pila_score
global punteo_total
punteo_total = 0

lista_serpiente = ListaDoble() 
pila_score = PilaScore()

global bloques
bloques = ListaDoble()

global pila_total_puntos
pila_total_puntos = PilaScore() 


#retorna lista serpiente vacia
def resetear_snake():
    snake_limpio = ListaDoble()
    return snake_limpio

#retorna pila puntos vacia
def resetear_pila_score():
    limpio_pilapuntuje = PilaScore() 
    return limpio_pilapuntuje

#retorna lista bloques vacia
def resetear_bloques():
    bloques_limpio = ListaDoble()
    return bloques_limpio



#Imprimir vacios de la serpiente
def imprimir_vacios():
    temporal = lista_serpiente.primer
    while (temporal != None):   
        window.addch(temporal.posy ,temporal.posx,' ') 
        temporal = temporal.siguiente

#imprimir serpiente
def impri_serpiente():
    temporal = lista_serpiente.primer
    while (temporal != None):        
        window.addch(temporal.posy ,temporal.posx,'#')
        temporal = temporal.siguiente

#cambio de direccion, retorna serpiente invertida
def cambio_dir_ser():
    invertir_serp = ListaDoble()
    temporal = lista_serpiente.primer 
    while (temporal != None):   
        invertir_serp.insertar_inicio(temporal.posx, temporal.posy,  temporal.valor)
        temporal = temporal.siguiente
        
    return invertir_serp


def get_direccion():
    return tecla_antes

#graficar puntos
def graficar_pts_juego():
    pila_score.graficar_score()

#graficar snake
def graficar_ser_juego():
    lista_serpiente.graficar_serpiente()

#obtener  puntos totales
def get_pts_total():
    return pila_total_puntos.size



#verificando si se topa, retorna boleano
def serpiente_choque():
    perder = False

    cabeza_snake = lista_serpiente.primer
    while cabeza_snake.siguiente is not None:  
        cabeza_snake = cabeza_snake.siguiente     

    cabezax = cabeza_snake.posx
    cabezay = cabeza_snake.posy

    temporal_ch = lista_serpiente.primer  
    while temporal_ch.siguiente is not None:  
        if (temporal_ch.posx == cabezax and temporal_ch.posy == cabezay):
            perder = True
        temporal_ch = temporal_ch.siguiente


    ##viendo si se con las bloques
    if (nivel >= 2):
        temp_cho = lista_serpiente.primer 
        while (temp_cho != None): 
            temp_pare = bloques.primer 
            while (temp_pare != None): 
                if (temp_pare.posx == temp_cho.posx and temp_pare.posy == temp_cho.posy):
                    perder = True
                temp_pare = temp_pare.siguiente
            temp_cho = temp_cho.siguiente

    return perder

def Comer():
    global comida_enx
    global comida_eny
    comida_enx = random.randint(3,58)
    comida_eny = random.randint(3,18)

    global tip_comida
    tip_comida = random.randint(0,5)

    if (nivel >= 2): 
        tempp = bloques.primer
        while (tempp != None): 
            if (tempp.posy == comida_eny and tempp.posx == comida_enx): 
                comida_enx = random.randint(3,58)
                comida_eny = random.randint(3,18)           
            tempp = tempp.siguiente
           
    nodo_ser_temp = lista_serpiente.primer
    while (nodo_ser_temp != None): 
        if (nodo_ser_temp.posy == comida_eny and nodo_ser_temp.posx == comida_enx): 
            comida_enx = random.randint(3,58)
            comida_eny = random.randint(3,18)           
        nodo_ser_temp = nodo_ser_temp.siguiente

    

    if (tip_comida == 0 or tip_comida == 1 or tip_comida == 2 or tip_comida == 3 or tip_comida == 4):      
        window.addch(comida_eny,comida_enx,'+')  
    elif (tip_comida == 5):      
        window.addch(comida_eny,comida_enx,'*')


def print_title(win,var_u):

    titulo = " SNAKE RELOADED "
    x_start = round((60-len(titulo))/2)
    win.addstr(0,x_start,titulo)

    puntos_score = " Score: " + str(pila_score.size) + " "
    if var_u == None:
        var_u = ""
    
    player = " Usuario : " + var_u + " "
    win.addstr(0,3,puntos_score)    
    inix = round(58-len(player))
    win.addstr(0,inix,player) 

    p_total = "Total: " + str(pila_total_puntos.size ) + " "
    niv_juego = "Nivel(" + str(nivel) + ")"
    win.addstr(19,3,p_total) 
    win.addstr(19,25,niv_juego) 

def ganar_niv():
    ganar = False
    if pila_score.size == 15:
        ganar = True
        
    return ganar


def imprimir_bloques():
    temp_pard = bloques.primer
    while (temp_pard != None):        
        window.addch(temp_pard.posy ,temp_pard.posx,'=') 
        temp_pard = temp_pard.siguiente


def imprimir_bloques_nada():
    temp_pard = bloques.primer
    while (temp_pard != None):        
        window.addch(temp_pard.posy ,temp_pard.posx,' ') 
        temp_pard = temp_pard.siguiente





def jugar(name_jug, continue_juego, direccion):
    global lista_serpiente
    global window
    global pila_score
    global pila_total_puntos

    global nivel
    global bloques
    # continue_juego true continuar juego 
    #                false nuevo juego 

    stdscr = curses.initscr()
    height = 20
    width = 60

    ypos = 0
    xpos = 0

    y_par1 = 0
    #nivel = 1
    
    window = curses.newwin(height,width,ypos,xpos) 
    window.keypad(True)     #enable Keypad mode
    curses.noecho()         #prevent input from displaying in the screen
    curses.curs_set(0)      #cursor invisible (0)
    window.border(0)        #default border for our window
    window.nodelay(True)    #return -1

    global key
    global tecla_antes


    if continue_juego == False:
        key = KEY_RIGHT         
        tecla_antes = KEY_RIGHT         

        lista_serpiente = resetear_snake()
        pila_score = resetear_pila_score()
        pila_total_puntos = resetear_pila_score()
        bloques = resetear_bloques()
    elif continue_juego == True:
        key = direccion
        tecla_antes = direccion

    if continue_juego == False:
        xpos = 5               
        ypos = 5               

    rapidez = 100    

    #Crear serpiente con 3 nodos
    if continue_juego == False:
        lista_serpiente.insertar_fin(xpos, ypos, None)
        xpos += 1
        lista_serpiente.insertar_fin(xpos, ypos, None)
        xpos += 1
        lista_serpiente.insertar_fin(xpos, ypos, None)
        nivel = 1


    elif continue_juego == True:
        pos_guardada = lista_serpiente.primer
        while pos_guardada.siguiente is not None:  
            pos_guardada = pos_guardada.siguiente      
        xpos = pos_guardada.posx
        ypos = pos_guardada.posy

        if (nivel >= 2):
            par_guardada = bloques.primer
            while par_guardada.siguiente is not None:  
                par_guardada = par_guardada.siguiente      
            y_par1 = par_guardada.posy
    
    Comer()
    print_title(window,name_jug)

    while key != 27:
        ganado = ganar_niv()
        if ganado == True:
            nivel += 1 
            while True:
                tecla = window.getch()
                window.clear()                         
                window.border(0) 
                titulo = "*** MUY BIEN, PASA nivel(" + str(nivel) + ") ***"
                x_start = round((60-len(titulo))/2)
                window.addstr(0,x_start,titulo)

                puntos_score = " Score: " + str(pila_score.size) + " "
                window.addstr(0,3,puntos_score)
                if tecla == 10:
                    pila_score = resetear_pila_score()
                    lista_serpiente = resetear_snake()
                    bloques = resetear_bloques()

                    print_title(window,name_jug)
                    xpos = 5        
                    ypos = 5 
                    lista_serpiente.insertar_fin(xpos, ypos, None)
                    xpos = xpos + 1
                    lista_serpiente.insertar_fin(xpos, ypos, None)
                    xpos = xpos + 1
                    lista_serpiente.insertar_fin(xpos, ypos, None)
                    key = KEY_RIGHT       
                    tecla_antes = KEY_RIGHT   

                    if (nivel >= 2):
                        y_par1 = 12
                        bloques.insertar_fin(ypar1,10, "b")
                        y_par1 = y_par1 +1
                        bloques.insertar_fin(ypar1,10, "b")
                        y_par1 = y_par1 +1
                        bloques.insertar_fin(ypar1,10, "b")
                        y_par1 = y_par1 +1
                        bloques.insertar_fin(ypar1,10, "b")
                        y_par1 = y_par1 +1
                        bloques.insertar_fin(ypar1,10, "b")

                    Comer()
                    break


        window.timeout(rapidez+50) 
        keystroke = window.getch()


        if (key == KEY_LEFT and tecla_antes == KEY_RIGHT):
            lista_serpiente = cambio_dir_ser()

        elif (key == KEY_RIGHT and tecla_antes == KEY_LEFT):
            lista_serpiente = cambio_dir_ser()

        elif (key == KEY_DOWN and tecla_antes == KEY_UP):
            lista_serpiente = cambio_dir_ser()
        
        elif (key == KEY_UP and tecla_antes == KEY_DOWN):
            lista_serpiente = cambio_dir_ser()

        if (nivel >= 2):
            imprimir_bloques_nada()
            bloques.delete_inicio()

        imprimir_vacios()
        
        lista_serpiente.delete_inicio()
        

        if key == KEY_RIGHT:                
            xpos = xpos + 1               
        elif key == KEY_LEFT:               
            xpos = xpos - 1               
        elif key == KEY_UP:               
            ypos = ypos - 1               
        elif key == KEY_DOWN:               
            ypos = ypos + 1
        
        if (nivel >= 2):    
            y_par1 = y_par1 + 1    

        #Si se come algo
        if (xpos == width - 1):
            xpos = 1
        elif (xpos == 0):
            xpos = 58

        if (ypos == height -1):
            ypos = 1
        elif (ypos == 0):
            ypos = 18

        if(xpos == comida_enx and ypos == comida_eny):
            if (tip_comida == 0 or tip_comida == 1 or tip_comida == 2 or tip_comida == 3 or tip_comida == 4):
                lista_serpiente.insertar_fin(xpos, ypos, None)
                pila_score.push(xpos, ypos, None)
                pila_total_puntos.push(xpos, ypos, None)

            elif (tip_comida == 5):
    
                size_serpiente = lista_serpiente.size
                if (size_serpiente >= 3):
                    lista_serpiente.delete_inicio()
                    pila_score.pop()
                    pila_total_puntos.pop()

            impri_serpiente()
            print_title(window, name_jug)

            if (tip_comida == 0 or tip_comida == 1 or tip_comida == 2 or tip_comida == 3 or tip_comida == 4):
                if key == KEY_RIGHT:               
                    xpos = xpos + 1               
                elif key == KEY_LEFT:              
                    xpos = xpos - 1               
                elif key == KEY_UP:                 
                    ypos = ypos - 1              
                elif key == KEY_DOWN:               
                    ypos = ypos + 1              
        
            Comer()

        if (key == KEY_LEFT and tecla_antes == KEY_RIGHT):
            temporal = lista_serpiente.primer
            while temporal.siguiente is not None:  
                temporal = temporal.siguiente      
        
            xpos = temporal.posx
            xpos = xpos - 1
            ypos = temporal.posy

            
        
        elif (key == KEY_RIGHT and tecla_antes == KEY_LEFT):
            temporal = lista_serpiente.primer
            while temporal.siguiente is not None:  
                temporal = temporal.siguiente      

            xpos = temporal.posx
            xpos = xpos + 1
            ypos = temporal.posy


        elif (key == KEY_DOWN and tecla_antes == KEY_UP):
            temporal = lista_serpiente.primer
            while temporal.siguiente is not None:  
                temporal = temporal.siguiente      

            xpos = temporal.posx
            ypos = temporal.posy
            ypos = ypos + 1


        elif (key == KEY_UP and tecla_antes == KEY_DOWN):
            temporal = lista_serpiente.primer
            while temporal.siguiente is not None:  
                temporal = temporal.siguiente      

            xpos = temporal.posx
            ypos = temporal.posy
            ypos = ypos - 1
        
        ####reaparecer
        if (xpos == width - 1): 
            xpos = 1
        elif (xpos == 0):
            xpos = 58
        
        if (ypos == height -1): 
            ypos = 1
        elif (ypos == 0): 
            ypos = 18

        if (y_par1 == width -1):
            y_par1 = 1
        elif (y_par1 == 0):
            y_par1 = 58


        if (nivel >= 2):
            bloques.insertar_fin(y_par1,10,"b")
            imprimir_bloques()

        lista_serpiente.insertar_fin(xpos, ypos, None) 
        impri_serpiente()

        tecla_antes = key
        if keystroke is not  -1:
            key = keystroke
        

        chocar = serpiente_choque()
        if (chocar == True):
            continue_juego = False
            key = 27
            
    
            
        
        ##PAUSAR
        if (key == 80 or key == 112):
            key = 27
            continue_juego = True
        
    curses.endwin()
    return continue_juego

    
