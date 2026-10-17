"""
E4.5 · Clase abstracta Figura con area() y perimetro();
implementa Circulo, Rectangulo y Cuadrado.
"""

from abc import ABC, abstractmethod
from math import pi

class Figura(ABC):
    @abstractmethod
    def area(self): ...

class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return pi * self.radio ** 2
    
    def perimetro(self):
        ...

class Rectangulo(Figura):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        ...

class Cuadrado(Figura):
    
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        ...



circulo = Circulo(10)
print(circulo.area())

rectangulo = Rectangulo(10,20)
print(rectangulo.area())

cuadrado = Cuadrado(10)
print(cuadrado.area())
