from datetime import date, datetime

class Horario:
    
    def __init__(self, fecha: date, hora: datetime):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def __str__(self):
        return f"Horario: {self.fecha} de {self.hora_inicio.strftime('%H:%M')} a {self.hora_fin.strftime('%H:%M')}"