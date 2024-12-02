from GestorLadrillo import GestorLadrillo
from GestorMaterial import GestorMaterial

def menu():
    gestormaterial = GestorMaterial()
    gestorladrillo = GestorLadrillo()
    gestorladrillo.cargaarchivo()
    gestormaterial.cargaarchivo()
    print("se cargo el gestor de ladrillos y materiales con exito")
    gestorladrillo.asignarmaterialesauto(gestormaterial)
    opcion = 0
    while opcion !=  4:
        print("""MENU DE OPCIONES
                1. Mostrar costo y caracteristicas de un material
                2. Mostrar costo total de fabricacion del pedido para cada ladrillo
                3. Mostrar listado
                4. Salir""")
        opcion = int(input("ingrese la opcion que desea elegir: "))
        if opcion == 1:
            idladrillo = int(input("ingrese el identificador de ladrillo: "))
            encontro = gestorladrillo.ladcostocarac(gestormaterial, idladrillo)
            if encontro == 0:
                print("no se encontro el ladrillo, asociado al id ingresado")
        elif opcion == 2:
            gestorladrillo.ladcostototal()
        elif opcion == 3:
            gestorladrillo.ladrillolistado()
        elif opcion == 4:
            print("saliendo del programa..")
        elif opcion >= 5:
            print("opcion no valida")