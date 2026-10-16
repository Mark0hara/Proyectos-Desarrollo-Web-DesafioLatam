class OrdenCompra():
    def nueva_orden(self):
        self.identificador = 0
        self.total_productos = 0
        self.monto = 0

    def asigna_monto(self, nuevo_monto: int):
        self.monto = nuevo_monto
        self.codigo_descuento = ""
        
        if nuevo_monto > 20000:
            self.codigo_descuento = "20PORCIENTO"
        elif nuevo_monto > 10000:
            self.codigo_descuento = "10PORCIENTO"