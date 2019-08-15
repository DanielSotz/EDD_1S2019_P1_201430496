import csv
from ListaCircularDoble import CircularDoble #para lista cicrular del usuario
lista_usuarios = CircularDoble()
class importar_csv:

    def importando(self, nombre_j):
        aceptado = False
        try:           
            archivo = open(nombre_j)
            reader = csv.DictReader(archivo)
            for row in reader:
                lista_usuarios.Insertar_nodo(row['Usuarios'])
            aceptado = True
        except:
            aceptado = False
        return aceptado

    def nuevo_us(self, nombre_j):
        lista_usuarios.Insertar_nodo(nombre_j)

    def retornar_lista_us(self):
        return lista_usuarios