"""
E4.1 · Clase CuentaBancaria con saldo privado, ingresar, retirar
(valida saldo suficiente) y propiedad saldo de solo lectura.
"""
# E4.1

class CuentaBancariaError (Exception):
    """  """


class CuentaBancaria:

    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    def retirar(self, cantidad):
        
        if not isinstance(cantidad, (int, float)):
            raise CuentaBancariaError("La cantidad no es float")
        
        if self._saldo < cantidad:
            raise CuentaBancariaError("Saldo insuficiente")
        
        self._saldo -= cantidad
        return True
    
    def ingresar(self, cantidad):
        
        if not isinstance(cantidad, (int, float)):
            raise CuentaBancariaError("La cantidad no es float")
        
        self._saldo += cantidad


c1 = CuentaBancaria("pepe",100)


try:
    c1.retirar(float(250))
    print(c1.saldo)

    c1.ingresar(float(100))
    print(c1.saldo)

except CuentaBancariaError as e:
    print(e)
    

