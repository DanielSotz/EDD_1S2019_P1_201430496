import os
class NodoDoble:
    def __init__(self, posx, posy, valor):    
        self.valor = valor
        self.posx = posx    
        self.posy = posy    

        self.siguiente = None       
        self.anterior =  None

class ListaDoble:
    
    def __init__(self):        
        self.primer = None 
        self.size = 0
        

    def esVacio(self):
        return self.primer == None

    #insertar nodo al principio
    def insertar_inicio(self, posx, posy, valor):    
        nuevo = NodoDoble(posx, posy, valor)
        if self.esVacio():    
           self.primer = nuevo
        else:      
            nuevo.siguiente  = self.primer
            self.primer = nuevo
            self.primer.anterior = nuevo

        self.size = self.size + 1

    #insertar nodo al final
    def insertar_fin(self, posx, posy, valor):
        nuevo = NodoDoble(posx, posy, valor)
        if self.esVacio():
            self.primer = nuevo
        else:
            temporal = self.primer
            while (temporal.siguiente is not None):
                temporal = temporal.siguiente
            temporal.siguiente = nuevo
            nuevo.anterior = temporal

        self.size = self.size + 1

    #eliminar nodo al principio
    def delete_inicio(self):
        if self.esVacio():    
            #lista doble vacia
            print("Lista Doble Vacia") 
        else:
        	aux = self.primer
        	self.primer = self.primer.siguiente
        	aux.siguiente = None
        	self.primer.anterior = None
        self.size = self.size - 1

    #eliminar nodo al final
    def delete_final(self):
        if self.esVacio():    
            #lista doble vacia
            print("Lista Doble Vacia") 
        else:           
            temporal = self.primer
            while temporal.siguiente is not None: 
                aux = temporal 
                temporal = temporal.siguiente   
            aux.siguiente = None
            temporal.anterior = None

        self.size = self.size - 1
            
    #Imprimir lista primero al ultimo
    def Lista_imprimir(self):   
        if self.esVacio():
            print ("La  lista doble esta vacia")
        else:
            temporal = self.primer
            while temporal != None:         
                print(str(temporal.posx) + ","+ str(temporal.posy) )       
                temporal = temporal.siguiente   

    # graficar grapiz
    def graficar_serpiente(self):

        f = open("list_serpiente.dot", "w")

        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape=record];\n")

        temporal = self.primer
          
        contador = 0
        while temporal != None:    
            
            nodo_name = str(contador)
            nodo_corde = "(" + str(temporal.posx) + "," + str(temporal.posy) + ")"
            f.write("node"+ nodo_name +"[label = \"{<f0>|<f1> "+ nodo_corde +"|<f2> }\"];\n")  
            
            if (temporal.anterior == None):
                f.write("node_n1[label = \"null\"];\n")  
                f.write("node"+ nodo_name +":f0 -> node_n1;\n" )           
            
            f.write("node"+ nodo_name +"-> ")


            temporal = temporal.siguiente
            contador = contador +1

            if (temporal != None):                
                nodo_name_sig = str(contador)
                nodo_name_ante = str(contador - 1)
                f.write("node"+ nodo_name_sig +";\n")
                f.write("node"+ nodo_name_sig +"-> node" + nodo_name_ante+";\n")

            else:
                f.write("node_n2;\n")  
                f.write("node_n2[label = \"null\"];\n")   

        f.write("}")
        f.close()

        os.system("dot -Tpng list_serpiente.dot -o list_serpiente.jpg")
        os.system("list_serpiente.jpg")

   
   


#lis_dob = ListaDoble()


 
#lis_dob.insertar_fin(7,2,"ju1")
#lis_dob.insertar_fin(8,2,"ju2")
#lis_dob.insertar_fin(9,2,"ju3*")

#lis_dob.graficar_serpiente()    
    