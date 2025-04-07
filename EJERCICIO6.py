class Empleado:
    contador_empleados = 0  # Atributo de clase para contar empleados

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario if salario > 0 else 0
        Empleado.contador_empleados += 1
    
    @classmethod
    def cantidad_empleados(cls):
        return cls.contador_empleados

# Ejemplo de uso
empleado1 = Empleado("Ana López", 2500)
empleado2 = Empleado("Carlos Gómez", 3200)

print(f"Número total de empleados: {Empleado.cantidad_empleados()}")
