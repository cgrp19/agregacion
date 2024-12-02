from ClaseLadrillo import *
from ClaseMaterial import *
import csv
import random

class GestorLadrillo():
    __listaladrillo = list

    def __init__(self) -> None:
        """inicializa la lista de ladrillos"""
        self.__listaladrillo = []

    def agregarladrillo(self, unladrillo):
        """agrega una clase ladrillo, a la lista de ladrillo"""
        self.__listaladrillo.append(unladrillo)

    def cargaarchivo(self):
        """carga de un archivo csv, una lista de ladrillos"""
        with open('C:\\Users\\gasto\\.vscode\\POO\\Unidad 3\\Ejercicio 2\\Ladrillos.csv') as archivo:
            reader = csv.reader(archivo, delimiter = ';')
            next(reader)
            for fila in reader:
                can = int(fila[0])
                id =  int(fila[1])
                kg = float(fila[2])
                cos = float(fila[3])
                unladrillo = ladrillo(can, id, kg, cos)
                self.agregarladrillo(unladrillo)

    def asignarmaterialesmanual(self):
        """"le asigan a cada ladrillo, su material correspondiente"""
        print("--------------------------------------------------------------------")
        for ladrillo in self.__listaladrillo:
            agregar = input(f"El ladrillo {ladrillo.getId()} tiene material refractario que agregar: ")
            if agregar == "si":
                mat = int(input("ingrese el numero de material: "))
                carac = input("ingrese las caracteristicas del ladrillo: ")
                cant = float(input("ingrese la cantidad de material utilizado: "))
                costo = float(input("ingrese el costo adicional del ladrillo, en el caso de tenerlo: "))
                unmaterial = material(mat, carac, cant, costo)
                ladrillo.agregarmaterial(unmaterial)
            print("----------------------------------------------------------------")

    def asignarmaterialesauto(self, gestormaterial):
        """Asigna a cada ladrillo, un material correspondiente de forma aleatoria"""
        print("--------------------------------------------------------------------")
        material = gestormaterial.getLista()
        for ladrillo in self.__listaladrillo:
            agregar = input(f"El ladrillo {ladrillo.getId()} tiene material refractario que agregar: ")
            if agregar == "si":
                print(f"Asignando material al ladrillo {ladrillo.getId()}")
                mat = random.choice(material)
                ladrillo.agregarmaterial(mat)
            print("----------------------------------------------------------------")

    def ladcostocarac(self, gestormaterial, id):
        """"para un id de un ladrillo ingresado, muestra el costo del ladrillo y sus caracteristicas"""
        encontrado = 0
        i = 0
        while encontrado == 0 and i < len(self.__listaladrillo):
            if self.__listaladrillo[i].getId() == id:
                encontrado = 1
                print("Datos del Ladrillo: ")
                print(f"Costo: {self.__listaladrillo[i].getCosto()}")
                gestormaterial.MostrarCarac(i)
            else:
                i += 1
        return encontrado

    def ladcostototal(self):
        """muestra para cada ladrillo, el costo total de fabricacion que tiene"""
        costofijo = 0
        costoadi = 0
        print("--------------------------------------------------------------------")
        for ladrillo in self.__listaladrillo:
            costototal = ladrillo.getCosto()
            for material in ladrillo.getLista():
                costoadi = material.getCostoadicional()
                costototal += costoadi
            print(f"El ladrillo {ladrillo.getId()} tiene un costo total de {costototal}")
            print("----------------------------------------------------------------")

    def ladrillolistado(self):
        """muestra para cada ladrillo fabricado, un listado"""
        costototal = 0
        costoaso = 0
        material = str
        id = 0
        print("Nº Id:    Material:     Costo Asociado:")
        for ladrillo in self.__listaladrillo:
            id = ladrillo.getId()
            costototal = ladrillo.getCosto()
            for material in ladrillo.getLista():
                costoaso = material.getCostoadicional()
                material = material.getMaterial()
                costototal +=  costoaso
            print(f"{id}      \t\t{material}      \t\t{costototal}")