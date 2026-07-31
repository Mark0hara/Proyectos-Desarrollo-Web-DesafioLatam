#Metodo de instancia (no estaticos)
class Cuenta:
    def __init__(self, saldo: float):
        self.saldo = saldo

#Metodo de instancia sin retorno explicito (Devuelve None por defecto)        
    def depositar(self, monto: float) -> None:
        self.saldo += monto

#Metodo de instancia con retorno y parametros
    def retirar(self, monto: float) -> bool:
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        return False
