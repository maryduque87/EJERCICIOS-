class TarjetaCredito:
    def __init__(self, numero):
        self.numero = numero
    
    @staticmethod
    def validar_tarjeta(numero):
        numero = str(numero)[::-1]  # Invertir el número de tarjeta
        suma = 0
        for i, digito in enumerate(numero):
            n = int(digito)
            if i % 2 == 1:  # Duplicar cada segundo dígito
                n *= 2
                if n > 9:
                    n -= 9  # Restar 9 si el número es mayor que 9
            suma += n
        return suma % 10 == 0

# Ejemplo de uso
tarjeta = TarjetaCredito("4532015112830366")
print(f"Número de tarjeta: {tarjeta.numero}")
print(f"Es válida: {TarjetaCredito.validar_tarjeta(tarjeta.numero)}")
