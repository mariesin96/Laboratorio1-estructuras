# Definición de la clase Coche
class Coche:
    def __init__(self, marca, modelo, año):
        # Atributos del coche
        self.marca = marca
        self.modelo = modelo
        self.año = año

    # Método para mostrar la información del coche
    def mostrar_info(self):
        print(f"Coche: {self.marca} {self.modelo} ({self.año})")

    # Método para simular arrancar el coche
    def arrancar(self):
        print(f"El {self.marca} {self.modelo} ha arrancado.")

# Creación de un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla", 2020)

# Ejecución de métodos del objeto
mi_coche.mostrar_info()
mi_coche.arrancar()