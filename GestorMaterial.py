from ClaseMaterial import *
import csv

class GestorMaterial:
    __listamaterial = list

    def __init__(self) -> None:
        self.__listamaterial = []

    def agregarmaterial(self, unmaterial):
        """agrega un objeto material, a la lista de un material"""
        self.__listamaterial.append(unmaterial)

    def getLista(self):
        """devuelve la lista"""
        return self.__listamaterial
    
    def cargaarchivo(self):
        """"carga de un archivo csv, una lista de los materiales"""
        with open('C:\\Users\\gasto\\.vscode\\POO\\Unidad 3\\Ejercicio 2\\Material.csv') as archivo:
            reader = csv.reader(archivo, delimiter = ';')
            next(reader)
            for fila in reader:
                mat = int(fila[0])
                car = fila[1]
                cant = float(fila[2])
                cos =  float(fila[3])   
                unmaterial = material(mat, car, cant, cos)
                self.agregarmaterial(unmaterial)

    def MostrarCarac(self, i):
        print(f"Caracteristicas del material: {self.__listamaterial[i].getCaracteristicas()}")