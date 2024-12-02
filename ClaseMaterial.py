class material:
    __material = int
    __caracteristicas = str
    __cantutilizada = float
    __costoadicional = float

    def __init__(self, mat, car, can,cos) -> None:
        self.__material = mat
        self.__caracteristicas = car
        self.__cantutilizada = can
        self.__costoadicional = cos

    def getMaterial(self):
        return self.__material
    
    def getCaracteristicas(self):
        return self.__caracteristicas
    
    def getCantutilizada(self):
        return self.__cantutilizada
    
    def getCostoadicional(self):
        return self.__costoadicional