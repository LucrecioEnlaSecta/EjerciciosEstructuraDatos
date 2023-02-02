#-------------------------------------------------------------------------------
# Name:        Ejercicio 1
# Purpose:
#
# Author:      lucas
#
# Created:     22/11/2022
# Copyright:   (c) lucas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Ejercicio 1
#Determinar el número de ocurrencias de un determinado elemento en una pila.

def main():
#Creamos el array de elementos y el de ocurrencias de cada elemento
    elementos=[2,3,3,1,2,3,4,4,5,4,5,4,3,4,4,2,5,6,7,7,8]
    ocurrencias=[0,0,0,0,0,0,0,0,0]
    miPila=Pila()
#Apilamos los elementos
    for i in range(0,len(elementos)-1):
        miPila.apilar(elementos[i])

#calculamos las ocurrencias
    while(not miPila.pila_vacia()):
        dato=miPila.desapilar()
        ocurrencias[dato-1]+=1
#imprimimos las ocurrencias del elemento solicitado
    datovich=int(input('Ingrese el numero que quiere saber la ocurrencia'))
    print(f'El numero de ocurrencias que tuvo el numero {datovich} es {ocurrencias[datovich-1]}')


    pass
class nodoPila(object) :
    """Clase nodo pila"""
    info, sig = None, None

class Pila(object) :
    """Clase Pila"""
    def __init__(self) :
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato) :
        """Apila el elemento sobre la cima de la pila"""
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = self.cima

        self.cima = nodo
        self.tamanio += 1

    def desapilar(self) :
        """Desapila el elemento de la cima de la pila y lo devuelve"""
        x = self.cima.info
        self.cima = self.cima.sig
        self.tamanio -= 1

        return x

    def pila_vacia(self) :
        """Devuelve true si la pila está vacía"""
        return self.cima is None

    def en_cima(self) :
        """Devuelve el valor almacenado en la cima de la pila"""
        if self.cima is not None :
            return self.cima.info
        else :
            return None

    def tamanio(self) :
        """Devuelve el nro de elementos en la pila"""
        return self.tamanio
if __name__ == '__main__':
    main()
