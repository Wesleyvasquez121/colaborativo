"""Un hotel de playa cuenta con un recepcionista que se encarga de
presentar a los clientes las opciones de habitaciones disponibles junto
con sus precios. Tras la elección de la habitación, el recepcionista
solicita los datos personales del cliente y el número de noches que
permanecerá en el hotel. Finalmente, entrega al cliente una factura
detallada con el total de los gastos.
 Adicionalmente, los clientes pueden solicitar servicios extra,
como el uso de la piscina o la cancha de golf, que tienen un costo
adicional. Implementa esta funcionalidad en tu programa"""

class Hotel:
    def __init__(self):
        self.habitaciones = {
            "Sencilla": 50,
            "Doble": 80,
            "Suite": 120
        }
        self.servicios_extra = {
            "Piscina": 10,
            "Cancha de Golf": 20
        }

    def mostrar_habitaciones(self):
        print("Opciones de habitaciones disponibles:")
        for habitacion, precio in self.habitaciones.items():
            print(f"{habitacion}: ${precio} por noche")

    def calcular_total(self, habitacion, noches, extras):
        total = self.habitaciones[habitacion] * noches
        for extra in extras:
            total += self.servicios_extra[extra]
        return total

    def generar_factura(self, nombre, habitacion, noches, extras):
        total = self.calcular_total(habitacion, noches, extras)
        print("\nFactura detallada:")
        print(f"Cliente: {nombre}")
        print(f"Habitación: {habitacion} - ${self.habitaciones[habitacion]} por noche")
        print(f"Noches: {noches}")
        for extra in extras:
            print(f"Servicio extra: {extra} - ${self.servicios_extra[extra]}")
        print(f"Total a pagar: ${total}")

def main():
    hotel = Hotel()
    hotel.mostrar_habitaciones()
    
    nombre = input("Ingrese su nombre: ")
    habitacion = input("Elija una habitación: ")
    noches = int(input("Número de noches: "))
    
    extras = []
    while True:
        extra = input("¿Desea algún servicio extra (Piscina, Cancha de Golf)? (escriba 'no' para terminar): ")
        if extra.lower() == 'no':
            break
        if extra in hotel.servicios_extra:
            extras.append(extra)
        else:
            print("Servicio no disponible.")
    
    hotel.generar_factura(nombre, habitacion, noches, extras)

if __name__ == "__main__":
    main()
