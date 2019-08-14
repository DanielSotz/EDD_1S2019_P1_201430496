import os
class NodoFila:
    def __init__(self, nombre, puntos):    
        self.nombre = nombre
        self.puntos = puntos    

        self.siguiente = None     


class Fila:
    def __init__(self):        
        self.primer = None 
        self.size = 0
        self.ultimo = None

    def esVacio(self):
        return self.primer is None

    #insertar
    def insertar_Nodo(self, nombre, puntos):
        
        nuevo = NodoFila(nombre, puntos)
        
        if self.esVacio():    
            self.primer = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.size += 1

        #eliminando mayor a 10
        maximo = self.size
        #print("maximo: "+ str(maximo) + " - " + nombre)
        if (maximo > 10):
            self.eliminar_Nodo()

    #primero en salir
    def eliminar_Nodo(self):
        if self.esVacio():
            print ("La lista esta vacia")
        elif self.primer == self.ultimo:
            self.primer = None
            self.ultimo = None
            self.size -= 1
        else:
            aux = self.primer
            self.primer = self.primer.siguiente
            aux.siguiente = None
            self.size -= 1


    #Imprimir fila
    def fila_imprimir(self):
        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temporal = self.primer
            while temporal != None:                    
                temporal = temporal.siguiente

    #graf puntuaciones                
    def graficar_puntuaciones(self):

        f = open("puntuaciones.dot", "w")

        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape=record];\n")
        contador = 0
        temporal = self.primer   
        while temporal != None:    
            nodo_nombre = "nod" + str(contador)
            nodo_corde = "(" + str(temporal.nombre ) + "," + str(temporal.puntos ) + ")"
            f.write( nodo_nombre +"[label = \"{<f1> "+ nodo_corde +"|<f2> }\"];\n")  
                  
            f.write(nodo_nombre +"-> ")

            temporal = temporal.siguiente
            contador += 1

            if (temporal != None):
                nodo_nombre_sig = "nod" + str(contador)
                f.write(nodo_nombre_sig +";\n")
            else:
                f.write("null;\n")  

        f.write("}")
        f.close()

        os.system("dot -Tpng puntuaciones.dot -o fila_puntuaciones.jpg")
        os.system("fila_puntuaciones.jpg")
            
'''            
filaprueba = Fila()
filaprueba.insertar_Nodo("j1", 1)
filaprueba.insertar_Nodo("j2", 2)
filaprueba.insertar_Nodo("j3", 3)
filaprueba.insertar_Nodo("j4", 4)
filaprueba.insertar_Nodo("j5", 5)
filaprueba.insertar_Nodo("j6", 6)
filaprueba.insertar_Nodo("j7", 7)
filaprueba.insertar_Nodo("j8", 8)
filaprueba.insertar_Nodo("j9", 9)
filaprueba.insertar_Nodo("j10", 10)
filaprueba.insertar_Nodo("j11",11)
filaprueba.insertar_Nodo("j12", 12)


filaprueba.graficar_puntuaciones()
'''
