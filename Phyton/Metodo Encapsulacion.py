class CuentaBancaria:
  def __init__(self, saldo):
    self.__saldo = saldo  # Atributo privado

  @property
  def saldo(self):
    return self.__saldo

  @saldo.setter
  def saldo(self, nuevo_saldo):
    if nuevo_saldo >= 0:
      self.__saldo = nuevo_saldo
    else:
      raise ValueError("El saldo no puede ser negativo.")

  def depositar(self, cantidad):
    self.__saldo += cantidad

  def retirar(self, cantidad):
    if cantidad <= self.__saldo:
      self.__saldo -= cantidad
    else:
      print("Fondos insuficientes")

      