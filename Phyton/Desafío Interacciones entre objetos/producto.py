class Producto:
    def __init__(self, nombre: str, precio: int, stock: int = 0):
        self.__nombre = nombre
        self.__precio = precio
        # El stock no puede ser menor a 0
        self.__stock = stock if stock >= 0 else 0

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value: int):
        """Permite modificar el stock, asegurando que nunca sea negativo."""
        self.__stock = value if value >= 0 else 0

    def __add__(self, other):
        """Sobrecarga para sumar stock al ingresar un producto existente."""
        if isinstance(other, Producto) and self.__nombre == other.nombre:
            self.stock += other.stock
        return self

    def __sub__(self, other):
        """Sobrecarga para restar stock al realizar una venta."""
        if isinstance(other, Producto) and self.__nombre == other.nombre:
            self.stock -= other.stock
        return self

    def __eq__(self, other):
        """Comparación por nombre para identificar productos únicos."""
        if isinstance(other, Producto):
            return self.__nombre == other.nombre
        return False

    def __repr__(self):
        return f"Producto({self.__nombre}, ${self.__precio}, Stock: {self.__stock})"