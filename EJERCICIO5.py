class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo if saldo >= 0 else 0
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            raise ValueError("La cantidad a depositar debe ser mayor que cero.")
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            raise ValueError("Fondos insuficientes o cantidad inválida.")
    
    def consultar_saldo(self):
        return self.saldo

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, interes_anual):
        super().__init__(titular, saldo)
        if 0 <= interes_anual <= 100:
            self.__interes_anual = interes_anual
        else:
            raise ValueError("El interés anual debe estar entre 0 y 100.")
    
    def aplicar_interes(self):
        self.saldo += self.saldo * (self.__interes_anual / 100)
    
    def consultar_interes(self):
        return self.__interes_anual

# Ejemplo de uso
cuenta = CuentaAhorro("Maria Duque", 1000, 5)
print(f"Saldo inicial: ${cuenta.consultar_saldo()}")

cuenta.aplicar_interes()
print(f"Saldo después de aplicar interés: ${cuenta.consultar_saldo()}")

print(f"Interés anual: {cuenta.consultar_interes()}%")
