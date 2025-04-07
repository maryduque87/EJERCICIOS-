class Libro:
    def __init__(self, titulo, autor, total_paginas):
        if total_paginas > 0:
            self.__titulo = titulo
            self.__autor = autor
            self.__total_paginas = total_paginas
            self.__pagina_actual = 1
        else:
            raise ValueError("El número total de páginas debe ser mayor que cero.")

    def avanzar_paginas(self, paginas):
        if self.__pagina_actual + paginas <= self.__total_paginas:
            self.__pagina_actual += paginas
        else:
            raise ValueError("No puedes avanzar más allá del número total de páginas.")

    def retroceder_paginas(self, paginas):
        if self.__pagina_actual - paginas >= 1:
            self.__pagina_actual -= paginas
        else:
            raise ValueError("No puedes retroceder más allá de la página 1.")
    
    def obtener_pagina_actual(self):
        return self.__pagina_actual
    
    def obtener_informacion(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor}, Total de páginas: {self.__total_paginas}, Página actual: {self.__pagina_actual}"

# Ejemplo de uso
libro = Libro("1984", "George Orwell", 328)
print(libro.obtener_informacion())

libro.avanzar_paginas(50)
print(f"Página actual después de avanzar: {libro.obtener_pagina_actual()}")

libro.retroceder_paginas(20)
print(f"Página actual después de retroceder: {libro.obtener_pagina_actual()}")
