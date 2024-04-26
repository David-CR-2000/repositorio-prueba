class Pelicula:
    def __init__(self,titulo, clasificacion_edad, duracion,director):
        self.titulo = titulo
        self.clasificacion_edad = clasificacion_edad
        self.duracion = duracion 
        self.director= director 
        
    


class Sala:
    def __init__(self,numero,capacidad, tipo_proyeccion, asientos):
        self.numero = numero
        self.capacidad = capacidad
        self.tipo_proyeccion = tipo_proyeccion
        self.asientos = asientos

        
    def verificar_disponibilidad(self):
        return self.asientos <= 200
    
    def entradas(self):
        pass
    
    
    def vender_entradas(self, precio):
        pass



class Cartelera:
    def menu(self):
        lista_peñicula = []
        num_salas = []
        num_butacas = []
        asientos_disponibles = 200
        asientos_ocupados = 0
        while True:
            print("Opciones:")
            print("---------------------")
            print("1.Añadir Pelicula.")
            print("2.Añadir Sala")
            print("3.Añadir Sesion")
            print("4.Mostrar cartelera de programación")
            print("5.Vender entrada")
            menu = int(input("Elija una opción (1-5): "))
            if menu == 1:
                titulo_usuario =  input("Introduce el título de la película: ")
                peli = Pelicula(titulo=titulo_usuario, clasificacion_edad=7, duracion=120, director=None)
                lista_peñicula.append(peli)
            elif menu == 2:
                seleccionar_sala = int(input("Selecciona el numero de la sala: "))
                salas = Sala(numero= seleccionar_sala, capacidad= 200, tipo_proyeccion= None, asientos= asientos_ocupados)
                num_salas.append(salas)
            elif menu == 3:
                pass
            elif menu == 4:
                pass
            elif menu == 5:
                venta_entradas = Sala(precio=8)
    def asignar_pelicula(self):
        pass
    def asignar_sala(self):
        pass

Cartelera().menu()