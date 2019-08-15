
import curses #import the curses library
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
from CargaMasiva import importar_csv




from ListaCircularDoble import CircularDoble

lista_usuarios = CircularDoble()

from Fila import Fila
fila_puntos = Fila()

import Juego

jugador_actual = None
continuacion_juego = False
dire = 'KEY_RIGHT'

datos_import = importar_csv()

def paint_menu(win):
    paint_title(win,' MAIN MENU ')          
    win.addstr(7,21, '1. Empezar juego')             
    win.addstr(8,21, '2. Tabla de puntuaciones')       
    win.addstr(9,21, '3. Seleccionar usuario')   
    win.addstr(10,21, '4. Reportes')         
    win.addstr(11,21, '5. Carga masiva')    
    win.addstr(12,21, '6. Nuevo jugador')
    win.addstr(13,21, '7. Exit')             
    win.timeout(-1)                        

def paint_title(win,var):
    win.clear()                         
    win.border(0)                
    x_start = round((66-len(var))/2)    
    win.addstr(0,x_start,var)           

def wait_esc(win):
    key = window.getch()
    while key!=27:
        key = window.getch()

def paint_reports(win):
    paint_title(win,' REPORTS ')         
    win.addstr(7,21, '1. Snake Report')            
    win.addstr(8,21, '2. Score Report')      
    win.addstr(9,21, '3. Scoreboard Report')  
    win.addstr(10,21, '4. Users Report')        
    win.addstr(12,21, '(ESC). Salir')               

def paint_pts_puntos(win):
    paint_title(win,' 2 -Tabla de Puntuciones')         
    win.addstr(3,18, 'Nombre')     
    win.addstr(3,41, 'Punteo')  
    y_nam = 4      
    print_score = fila_puntos.primer
    while print_score != None:            
        win.addstr(y_nam,18, str(print_score.nombre)) 
        win.addstr(y_nam,41, str(print_score.puntos ))           
        print_score = print_score.siguiente
        y_nam = y_nam +1

        
    win.addstr(16,21, '(ESC). Salir')      
               
def scoreboard(win):
    
    while True:
        paint_pts_puntos(win)
        tecla = window.getch()
        if tecla == 27:
            break

#para seleccionar reportes
def seleccion_reportes(win):
     
    while True:
        paint_reports(win)
        tecla = window.getch()
        
        if tecla == 49: #1
            Juego.graficar_ser_juego()
        elif tecla == 50: #2
            Juego.graficar_pts_juego()
        elif tecla == 51: #3
            fila_puntos.graficar_puntuaciones()
        elif tecla == 52: #4
            paint_title(win, '4. Users Report')
            usuario_jugando = lista_usuarios.cabeza
            if (usuario_jugando == None):
                pintar_usuarios(win, "No tiene usuarios ingresados")
                while True:
                    tecla = window.getch()
                    if tecla == 27:
                        break
            else:
                lista_usuarios.graficar_usuarios()

            
        elif tecla == 27:
            break


#empezar a jugar
def empezar_snake(win):
    bandera_continuacion = False
    global jugador_actual
    if (jugador_actual == None):
        pintar_usuarios(win, "Ningun Jugador Seleccionado")  
        win.addstr(7,21, 'N. Nuevo Jugador')            
        while True:
            tecla = win.getch()
            if tecla == 110 or tecla == 78:
                paint_title(win," Nuevo Jugador ")
                win.addstr(3,21, 'Ingrese numbre de jugador')  

                win.keypad(False)    
                curses.echo()         
                curses.curs_set(1)     
                nombre_archivo  = win.getstr(6,20).decode(encoding="utf-8")

                jugador_actual = nombre_archivo
                datos_import.nuevo_us(jugador_actual)

                win.keypad(True)    
                curses.noecho()         
                curses.curs_set(0)
                empezar_snake(win)
                tecla = 27
                break

            elif tecla == 27:
                break
    else:
          
        while True:
            paint_title(win," Empezar Juego")
               
            des = 'Presione Enter'
            x_start = round((60-len(des))/2)
            win.addstr(8,x_start, des) 

            tecla = win.getch()

            if tecla == 10:
                global continuacion_juego
                
                global dire
                bandera_continuacion = Juego.jugar(jugador_actual, continuacion_juego, dire)
                continuacion_juego = bandera_continuacion
                if (bandera_continuacion== False):
                    paint_title(win," PERDISTE ")
                    des = 'Game Over'
                    x_start = round((60-len(des))/2)
                    win.addstr(8,x_start,des) 
                    pts =Juego.get_pts_total()
                    fila_puntos.insertar_Nodo(jugador_actual, pts)   

                    while True:
                        if win.getch() == 27:
                            Juego.graficar_ser_juego()
                            break
                elif (bandera_continuacion== True):
                    paint_title(win," Presione Enter ")
                    dire = Juego.get_direccion()
                    des = 'PAUSADO'
                    x_start = round((60-len(des))/2)
                    win.addstr(8,x_start,des) 
 
                    win.getch()
                    break
                break
            elif tecla == 27:
                break

            
def obtener_list_usu():
    global lista_usuarios
    lista_usuarios = datos_import.retornar_lista_us()

def seleccion_usuarios(win):

    obtener_list_usu()
    usuario_jugando = lista_usuarios.cabeza  

    if (usuario_jugando == None):
        pintar_usuarios(win, "No tiene usuarios ingresados")
        while True:
            tecla = window.getch()
            if tecla == 27:
                break
    else:     
        nombre_usactual = usuario_jugando.usuario
        nombre_usactual = "<--- " + nombre_usactual + " --->"
        pintar_usuarios(win, nombre_usactual)
        while True:
            tecla = win.getch()
            if tecla == curses.KEY_RIGHT:
                usuario_jugando = usuario_jugando.siguiente

                paint_title(window,' 3 - Seleccion de Usuarios ')
                nombre_usactual = usuario_jugando.usuario
                nombre_usactual = "<--- " + nombre_usactual + " --->"
                pintar_usuarios(win, nombre_usactual)
        
            elif tecla == curses.KEY_LEFT:
                usuario_jugando = usuario_jugando.anterior

                paint_title(window,' 3 - Seleccion de Usuarios ')
                nombre_usactual = usuario_jugando.usuario
                nombre_usactual = "<--- " + nombre_usactual + " --->"
                pintar_usuarios(win, nombre_usactual)

            elif tecla == 10:
                global jugador_actual
                jugador_actual = usuario_jugando.usuario
                break
            elif tecla == 27:
                break
            
    

def pintar_usuarios(win, user):
    altura = 20 
    ancho = 60

    y = int(altura/2)
    x = int(int(ancho/2) - (len(user)/2))
    win.addstr(y,x, user )
    win.refresh()

def importacion_archivo(win):

    while True:
        tecla = window.getch()
        if tecla == 115 or tecla == 83: #S
            paint_title(window,' 5 - Carga Masiva')
            win.addstr(4,15, 'Ingrese Nombre de Arhivo y seguido de .csv') 

            win.keypad(False)    
            curses.echo()         
            curses.curs_set(1)     
            nombre_archivo  = win.getstr(6,20).decode(encoding="utf-8")
            
            arch_importado = False
            arch_importado = datos_import.importando(nombre_archivo)

            paint_title(window,' 5 - Carga Masiva ')
            if (arch_importado == True):
                global lista_usuarios
                lista_usuarios = datos_import.retornar_lista_us()
                window.addstr(8,5, '(Datos importados) Presione cualquier tecla para continuar')
            elif (arch_importado == False):
                window.addstr(8,5, 'Archivo no encontrado')
            
            
            win.keypad(True)    
            curses.noecho()         
            curses.curs_set(0) 

            tecla = window.getch()
            break

        elif tecla == 110:
            break

        elif tecla == 27:
            break

def nuevo_jugador(win):

    if (continuacion_juego == False):            
        while True:
            pintar_usuarios(win, "Seleccione")  
            win.addstr(7,21, 'N. Nuevo Jugador')  
            tecla = win.getch()
            if tecla == 110 or tecla == 78:
                paint_title(win," Nuevo Jugador ")
                win.addstr(3,21, 'Ingrese nombre de jugador')  

                win.keypad(False)    
                curses.echo()         
                curses.curs_set(1)     
                nombre_archivo  = win.getstr(6,20).decode(encoding="utf-8")

                jugador_actual = nombre_archivo
                datos_import.nuevo_us(jugador_actual)

                global lista_usuarios
                lista_usuarios = datos_import.retornar_lista_us()

                win.keypad(True)    
                curses.noecho()         
                curses.curs_set(0) 

                tecla = 27
                break

            elif tecla == 27:
                break
    else:
        tecla = win.getch()
        pintar_usuarios(win, "No se puede crear")  
        win.addstr(7,21, 'hasta que termine el juego actual')    




stdscr = curses.initscr() #initialize console
window = curses.newwin(20,60,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)      #paint menu

keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    if(keystroke==49): #1
        paint_title(window, ' JUEGO ')
        empezar_snake(window)        
        paint_menu(window)
        keystroke=-1
    elif(keystroke==50):
        paint_title(window, ' Tabla de Puntuciones ')
        scoreboard(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51):
        paint_title(window, ' Selecion de Usuario ')
        seleccion_usuarios(window)
        paint_menu(window)
        keystroke=-1
        keystroke=-1
    elif(keystroke==52):
        paint_title(window, ' Seleccion de Reportes')
        seleccion_reportes(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==53):
        paint_title(window,' Carga Masiva ')
        window.addstr(7,21, '¿Desea importar archvivo csv usuarios?')            
        window.addstr(8,21, 'S/N')
        importacion_archivo(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==54):
        paint_title(window,' Nuevo Jugador ')
        nuevo_jugador(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==55):
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state