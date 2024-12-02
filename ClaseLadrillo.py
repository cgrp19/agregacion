class ladrillo:
    __alto = 7
    __largo = 25
    __ancho = 15
    __cantidad = int
    __id = int
    __kgmatuti = float
    __costo = float
    __material = list

    def __init__(self, can, id , kg, cos) -> None:
        self.__cantidad = can
        self.__id = id
        self.__kgmatuti = kg
        self.__costo = cos
        self.__material = []

    def getAlto(cls):
        return cls.__alto
    
    def getLargo(cls):
        return cls.__largo
    
    def getAncho(cls):
        return cls.__ancho
    
    def getCantidad(self):
        return self.__cantidad
    
    def getId(self):
        return self.__id
    
    def getKgmatuti(self):
        return self.__kgmatuti
    
    def getCosto(self):
        return self.__costo
    
    def agregarmaterial(self, unmaterial):
        self.__material.append(unmaterial)

    def getLista(self):
        return self.__material