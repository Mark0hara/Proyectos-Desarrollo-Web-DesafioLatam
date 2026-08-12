from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self, nombre: str, costo_delivery: int):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []  
    @property
    def nombre(self):
        return self.__nombre

    @property
    def productos(self):
        return self.__productos

    def ingresar_producto(self, nombre: str, precio: int, stock: int = 0):
        """Método base para ingresar productos. Usa Colaboración y Sobrecarga."""
        nuevo_producto = Producto(nombre, precio, stock)
        for p in self.__productos:
            if p == nuevo_producto:
                p + nuevo_producto  
                return
        
        self.__productos.append(nuevo_producto)

    @abstractmethod
    def listar_productos(self) -> str:
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto: str, cantidad: int):
        pass


class Restaurante(Tienda):
    def ingresar_producto(self, nombre: str, precio: int, stock: int = 0):
        super().ingresar_producto(nombre, precio, 0)

    def listar_productos(self) -> str:
        if not self.productos:
            return "No hay productos disponibles."
        lista = [f"{p.nombre} | ${p.precio}" for p in self.productos]
        return "\n".join(lista)

    def realizar_venta(self, nombre_producto: str, cantidad: int):
        pass


class Supermercado(Tienda):
    def listar_productos(self) -> str:
        if not self.productos:
            return "No hay productos disponibles."
        lista = []
        for p in self.productos:
            info = f"{p.nombre} | ${p.precio} | Stock: {p.stock}"
            if p.stock < 10:
                info += " - Pocas unidades disponibles"
            lista.append(info)
        return "\n".join(lista)

    def realizar_venta(self, nombre_producto: str, cantidad: int):
        for p in self.productos:
            if p.nombre == nombre_producto:
                if p.stock > 0:
                    venta_real = min(cantidad, p.stock)
                    p - Producto(nombre_producto, 0, venta_real)  # Colaboración __sub__
                return


class Farmacia(Tienda):
    def listar_productos(self) -> str:
        if not self.productos:
            return "No hay productos disponibles."
        lista = []
        for p in self.productos:
            info = f"{p.nombre} | ${p.precio}"
            if p.precio > 15000:
                info += " - Envío gratis al solicitar este producto"
            lista.append(info)
        return "\n".join(lista)

    def realizar_venta(self, nombre_producto: str, cantidad: int):
        if cantidad > 3:
            return 

        for p in self.productos:
            if p.nombre == nombre_producto:
                if p.stock > 0:
                    venta_real = min(cantidad, p.stock)
                    p - Producto(nombre_producto, 0, venta_real)
                return