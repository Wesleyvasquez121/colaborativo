class Empleado:
    def __init__(self, nombre, tipo, salario_base=0, horas_trabajadas=0, comisiones=0, años_trabajados=0):
        self.nombre = nombre
        self.tipo = tipo
        self.salario_base = salario_base
        self.horas_trabajadas = horas_trabajadas
        self.comisiones = comisiones
        self.años_trabajados = años_trabajados

    def calcular_pago(self):
        if self.tipo == "fijo":
            pago = self.salario_base + self.comisiones
        elif self.tipo == "horas":
            pago = self.horas_trabajadas * self.salario_base
        else:
            raise ValueError("Tipo de empleado no válido")

        if self.años_trabajados > 5:
            pago += 100  # Bono adicional

        return pago

def generar_planilla(empleados):
    print("Planilla de Pago:")
    for empleado in empleados:
        pago = empleado.calcular_pago()
        print(f"Empleado: {empleado.nombre}, Pago: ${pago}")

# Ejemplo de uso
empleados = [
    Empleado(nombre="Juan", tipo="fijo", salario_base=1000, comisiones=200, años_trabajados=6),
    Empleado(nombre="Ana", tipo="horas", salario_base=15, horas_trabajadas=160, años_trabajados=3),
    Empleado(nombre="Luis", tipo="fijo", salario_base=1200, comisiones=300, años_trabajados=10),
    Empleado(nombre="María", tipo="horas", salario_base=20, horas_trabajadas=120, años_trabajados=7)
]

generar_planilla(empleados)
