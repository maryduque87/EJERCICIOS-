class Estudiante:
    def __init__(self, nombre, edad):
        if edad > 0:
            self.__nombre = nombre
            self.__edad = edad
            self.__notas = []
        else:
            raise ValueError("La edad debe ser un número positivo.")

    def agregar_nota(self, nota):
        if 0 <= nota <= 100:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0 y 100.")
    
    def calcular_promedio(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

# Ejemplo de uso
estudiante = Estudiante("Maria Duque", 18)
print(f"Estudiante: {estudiante.obtener_nombre()}, Edad: {estudiante.obtener_edad()}")

estudiante.agregar_nota(3.5)
estudiante.agregar_nota(4.6)
estudiante.agregar_nota(5.0)

print(f"Promedio de notas: {estudiante.calcular_promedio():.2f}")
