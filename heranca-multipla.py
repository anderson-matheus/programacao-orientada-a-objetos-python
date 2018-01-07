class Relogio:
    def __init__(self, hora=0, minu=0, seg=0, *args, **kwargs):
        super(Relogio, self).__init__(*args, **kwargs)
        self.hora = hora
        self.minu = minu
        self.seg = seg

    def ajustar_hora(self, hora, minu, seg):
        self.hora = hora
        self.minu = minu
        self.seg = seg

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hora,
                                                self.minu,
                                                self.seg)
        # self.seg) + ' ' + super(Relogio, self).__str__()

    def tick(self):
        if self.seg == 59:
            self.seg = 0
            if self.minu == 59:
                self.minu = 0
                if self.hora == 23:
                    self.hora = 0
                else:
                    self.hora += 1
            else:
                self.minu += 1
        else:
            self.seg += 1


class Calendario:
    meses = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, dia, mes, ano, *args, **kwargs):
        super(Calendario, self).__init__(*args, **kwargs)
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def ajustar_data(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return "{0:02d}/{1:02d}/{2:4d}".format(self.dia, self.mes, self.ano)

    def avancar(self):
        dia_max = Calendario.meses[self.mes - 1]
        if self.dia == dia_max:
            self.dia = 1
            if self.mes == 12:
                self.mes = 1
                self.ano += 1
            else:
                self.mes += 1
        else:
            self.dia += 1


class CalendarioRelogio(Relogio, Calendario):
    def __init__(self, hora, minu, seg, dia, mes, ano):
        super(CalendarioRelogio, self).__init__(
            hora=hora, minu=minu, seg=seg, dia=dia, mes=mes, ano=ano)

    def __str__(self):
        return Relogio.__str__(self) + ' ' + Calendario.__str__(self)
        # return super(CalendarioRelogio, self).__str__()

    def tick(self):
        hora_anterior = self.hora
        Relogio.tick(self)
        if self.hora < hora_anterior:
            self.avancar()


print('Classe Relógio')
rel = Relogio(1, 59, 59)
print(rel)
rel.tick()
print(rel)
print('\n\n')

print('Classe Calendário')
cal = Calendario(30, 12, 2016)
print(cal)
cal.avancar()
print(cal)
print('\n\n')

print('Classe Calendário Relógio')
cal_rel = CalendarioRelogio(23, 59, 59, 31, 12, 2015)
print(cal_rel)
cal_rel.tick()
print(cal_rel)
print(CalendarioRelogio.mro())
