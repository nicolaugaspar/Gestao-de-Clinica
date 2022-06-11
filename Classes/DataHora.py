
ano = 0
mes = 0
dia = 0
hora = 0
minuto = 0


class Data():
    def __init__(self, dia, mes, ano):
        self.ano = ano
        self.mes = mes
        self.dia = dia
    def __str__(self):
        message = "{}/{}/{}"
        return message.format(str(self.dia), str(self.mes), str(self.ano))

class Hora():
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto
    def __str__(self):
        message = "{}:{}"
        return message.format(str(self.hora), str(self.minuto))