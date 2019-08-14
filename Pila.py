import os
class NodoPila:
    def __init__(self, posx, posy , valor):    
        self.valor = valor
        self.posx = posx    
        self.posy = posy    

        self.siguiente = None       

class PilaScore:
    def __init__(self):        
        self.primer = None 
        self.size = 0
        self.ultimo = None

    def esVacio(self):
        return self.primer is None
        

    #insertar hasta arriba
    def push(self, posx, posy, valor):
        
        nuevo = NodoPila(posx, posy, valor)
        
        if self.esVacio():    
            self.primer = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.size += 1


    #sacar el de hasta arriba
    def pop(self):  
        if self.esVacio():
            print (" La lista esta vacia") 
        elif self.primer == self.ultimo:
            self.primer = None
            self.ultimo = None 
        else:
            nodo_arriba = self.primer
            aux = None
            while nodo_arriba != None:
                if nodo_arriba.siguiente == self.ultimo:
                    
                    aux = self.ultimo
                    self.ultimo = nodo_arriba
                    nodo_arriba.siguiente = None
                else:
                    nodo_arriba = nodo_arriba.siguiente
        self.size -= 1


    #Imprimir lista
    def Pila_imprimir(self):
        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temporal = self.primer

            while temporal != None:         
                #print(str(temporal.posx) + ","+ str(temporal.posy) + " pila")     
                print( temporal.valor + " - " + str(temporal.posx) + ","+ str(temporal.posy) )          
                temporal = temporal.siguiente

    #Limpiar lista
    def Limpiar_pila(self):
        temporal = self.primer
        while temporal != None:         
            self.pop()       
            temporal = temporal.siguiente
        self.pop() 

    #para graficar en grapiz la pila score
    def graficar_score(self):

        f = open("pila.dot", "w")

        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape=record];\n")
        f.write("node0[label = \"")

        temporal = self.primer
        pila_cor = ""
        while temporal != None:    
            nodo_corde = "(" + str(temporal.posx) + "," + str(temporal.posy) + ")"
            pila_cor = "|" + nodo_corde  + pila_cor 
            temporal = temporal.siguiente
        f.write(str(pila_cor) + "\"")
        f.write("]; \n}")
        f.close()

        os.system("dot -Tpng pila.dot -o pila_puntaje.jpg")
        os.system("pila_puntaje.jpg")


#pilaprueba = PilaScore()
#pilaprueba.push(0, 0, "1")
#pilaprueba.push(1,1,"2")
#pilaprueba.push(2,2,"3")


#pilaprueba.pop()
#print("elimando")
#pilaprueba.Limpiar_pila()
#pilaprueba.Pila_imprimir()
#pilaprueba.graficar_score()