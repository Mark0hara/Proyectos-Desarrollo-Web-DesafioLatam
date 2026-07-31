class Paciente():
    def __init__(self, nombre:str, edad:int, direccion:str, fono:str):
        self._nombre = nombre
        self._edad = edad
        self._direccion = direccion
        self._fono = fono
        self._historial = []

@property
def nombre(self):
        return self._nombre

@property
def edad(self):
        return self._edad

@property
def direccion(self):
        return self._direccion

@property
def fono(self):
        return self._fono

@property
def historial(self) -> list:
        return self._historial 

@nombre.setter
def nombre(self, nombre:str):
        self._nombre = nombre

@edad.setter
def edad(self, edad:int):   
        self._edad = edad   

@direccion.setter
def direccion(self, direccion:str):
        self._direccion = direccion

@fono.setter
def fono(self, fono:str):
        self._fono = fono

def __str__(self):
        return (f"datos del paciente: {self._nombre}, Edad: {self._edad}, Dirección: {self._direccion}, Teléfono: {self._fono}")