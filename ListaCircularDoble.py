class NodoCircular:
    def __init__(self,  usuario = None, idusuario = None):
        self.idusuario = idusuario     
        self.usuario = usuario
        self.siguiente = None       
        self.anterior =  None

import os

class CircularDoble:
    def __init__(self):        
        self.cabeza = None 
        self.size = 0
        self.ultimo = None

    def esVacio(self):
        return self.cabeza is None

    #insertar nodo 
    def Insertar_nodo(self, usuario):
        nuevo = NodoCircular(usuario, self.size)

        if self.esVacio():
            self.cabeza = nuevo
            self.ultimo = nuevo

            self.cabeza.anterior = self.ultimo
            self.ultimo.siguiente = self.cabeza
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo

            self.cabeza.anterior = self.ultimo
            self.ultimo.siguiente = self.cabeza
            
        self.size = self.size + 1


    #Imprimir lista adelante
    def Lista_imprimir(self):
        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temporal = self.cabeza            
            while temporal != self.ultimo:         
                print(temporal.usuario + " - " + str(temporal.idusuario))            
                temporal = temporal.siguiente
            print(temporal.usuario + " - " + str(temporal.idusuario)) 

   


    def graficar_usuarios(self):

        f = open("lista_usuarios.dot", "w")

        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape=record];\n")

        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temporal = self.cabeza
            while temporal != self.ultimo:         
                
                nodo_actual =  str(temporal.idusuario)
                nodo_actual_sig = str(temporal.siguiente.idusuario)
                f.write("node"+ nodo_actual +"[label = \"{<f0>|<f1> "+ temporal.usuario +"|<f2> }\"];\n")            
                
                f.write("node"+ nodo_actual +" -> ")
                f.write("node"+ nodo_actual_sig +";\n") 

                f.write("node"+ nodo_actual_sig +" -> ")
                f.write("node"+ nodo_actual +";\n") 

                temporal = temporal.siguiente
            #print(temporal.usuario)
            nodo_actual =  str(temporal.idusuario)
            nodo_actual_sig = str(temporal.siguiente.idusuario)

            f.write("node"+ nodo_actual +"[label = \"{<f0>|<f1> "+ temporal.usuario +"|<f2> }\"];\n")

            f.write("node"+ nodo_actual +" -> ")
            f.write("node"+ nodo_actual_sig +";\n") 

            f.write("node"+ nodo_actual_sig +" -> ")
            f.write("node"+ nodo_actual +";\n") 

        f.write("}")
        f.close()

        os.system("dot -Tpng lista_usuarios.dot -o lista_usuarios.jpg")
        os.system("lista_usuarios.jpg")

    



#circular = CircularDoble()
#circular.Insertar_nodo("J1")
#circular.Insertar_nodo("J2")
#circular.Insertar_nodo("J3")
#circular.Insertar_nodo("J4")
#circular.Lista_imprimir()
#circular.graficar_usuarios()