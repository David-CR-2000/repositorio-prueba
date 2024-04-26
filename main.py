"""    
Crea las clases Bicicleta y Coche. Crea los atributos de instancia kilómetros_recorridos, 
kilómetros_totales y color. Crea también algún método específico para cada una de las clases, 
los que necesites para implementar el menú VEHÍCULOS. Prueba las clases creadas implementando dos objetos e interactuando con ellos 
mediante un programa con un menú como el que se muestra a continuación.

Dicho programa debe ir pidiendo datos al usuario para construir el objeto deseado, 
una vez creado el objeto debe aparecer el siguiente menú.

•Añade a los métodos ver kilometraje una opción en la que si la bicicleta tiene más de 10.000 kilómetros o el 
coche más de 100.000 recomiende cambiar el vehículo.
•Añade una opción por si se desea volver al menú de crear objeto.
•Ten en cuenta que solo podrá existir un objeto de cada, si el usuario decide crear uno nuevo los datos se 
sobrescribirán sobre el anterior

"""
class Vehiculos:
    def __init__(self, instancia, km_recorridos, km_totales, color):
        self.insancia = instancia
        self.km_recorridos = km_recorridos
        self.km_totales = km_totales
        self.color = color
    def menu():
        while True:
            print("¿Que objeto deseas crear?")
            print("1. Coche")
            print("2. Bicicleta")
            print("3. Ir al menú de vehiculos")
            print("4. Salir")
            menu = print(int(input("Elija una opción (1-9): ")))
            if menu == 1:
                pass
            elif menu == 2:
                pass
            elif menu == 3:
                pass
            elif menu == 4:
                break
            else:
                pass
        
        
class Bicicleta:
    
    def circular(self):
        instancia =  input("¿Qué tipo de instancia quieres? (ciclista o montador) ")
        km_recorridos =  float(input("Inserte la distancia recorrida: "))
        km_totales = km_recorridos
        
    def recomendar_cambio_de_rueda(self):
        if self.km_totales > 1000:
            print("Se recomienda cambiar la rueda de la bicicleta")
        
        


class Coche:
    def __init__(self, instancia, km_recorridos, km_totales, color):
        self.insancia = instancia
        self.km_recorridos = km_recorridos
        self.km_totales = km_totales
        self.color = color
        


        
Vehiculos.menu()