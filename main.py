import math


class Figura:
    """Clase base para representar una figura geométrica."""

    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    @property
    def nombre(self):
        return self.__nombre

    def area(self):
        pass

    def perimetro(self):
        pass

    def __str__(self):
        return f"Figura: {self.__nombre}"


class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.__radio = 0
        self.radio = radio  # Uso del setter para validar

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            print("Error: El radio debe ser mayor a cero.")
            self.__radio = 1  # Valor por defecto para evitar errores de ejecución
        else:
            self.__radio = valor

    def area(self):
        return math.pi * (self.__radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.__radio

    def __str__(self):
        return f"{super().__str__()} | Radio: {self.__radio:.2f}"


class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, valor):
        if valor > 0:
            self.__base = valor
        else:
            print("Base debe ser positiva")

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self.__altura = valor

    def area(self):
        return self.__base * self.__altura

    def perimetro(self):
        return 2 * (self.__base + self.__altura)

    def __str__(self):
        return f"{super().__str__()} | Base: {self.__base} | Altura: {self.__altura}"


# --- Bloque de ejecución para el taller ---
if __name__ == "__main__":
    print("-" * 30)
    print("TALLER DE POO - FIGURAS")
    print("-" * 30)

    # Lista de figuras para demostrar Polimorfismo
    mis_figuras = [
        Circulo(5),
        Rectangulo(10, 4),
        Circulo(2.5)
    ]

    for f in mis_figuras:
        print(f)
        print(f"Área: {f.area():.2f}")
        print(f"Perímetro: {f.perimetro():.2f}")
        print("-" * 20)

    # Prueba de validación (encapsulamiento)
    print("\nProbando validación de datos:")
    c_error = Circulo(-10)
    print(c_error)
