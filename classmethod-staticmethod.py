class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def de_string(cls, data_string):  # 14-01-2018
        dia, mes, ano = map(int, data_string.split('-'))
        data = cls(dia, mes, ano)
        return data

    @staticmethod  # não é herdado (é uma função dentro de uma classe)
    def is_date_valid(data_string):
        dia, mes, ano = map(int, data_string.split('-'))
        return dia <= 31 and mes <= 12 and ano <= 2020


data1 = Data(10, 10, 10)
data2 = Data.de_string('14-01-2018')
print(data2)
print(Data.is_date_valid('14-01-2018'))
