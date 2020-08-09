# import datetime
# data_atual = datetime.date.today()
# # data_atual_br = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
# data_atual_br = data_atual.strftime('%d/%m/%Y')
# data_hora_atual = datetime.datetime.now()
# hora_atual = datetime.datetime.date()
# print(data_atual)
# print()
# print(data_atual_br)
# print()
# print(data_hora_atual)
# print()
# print(hora_atual)
from datetime import date
data_atual = date.today()

class Pessoa:
    quant_filhos = 0
    def __init__(self, nome, dia_mes_ano):
        self.nome = nome
        dia_mes_ano = [int(i) for i in dia_mes_ano.split('/')]
# ------ definição da idade
        if data_atual.month > dia_mes_ano[1]:
            self.idade = data_atual.year - dia_mes_ano[2]
        elif data_atual.month == dia_mes_ano[1]:
            if data_atual.day >= dia_mes_ano[0]:
                self.idade = data_atual.year - dia_mes_ano[2]
            else:
                self.idade = data_atual.year - dia_mes_ano[2] - 1
        else:
            self.idade = data_atual.year - dia_mes_ano[2] - 1

    def cumprimentar(self):
        return f'Olá {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - quantidade de filhos={cls.quant_filhos}'


if __name__ == '__main__':
    p1 = Pessoa('Edivaldo', '11/04/1984')
    p1.quant_filhos = 3
    print(p1.cumprimentar())
    print(p1.__dict__)
    p2 = Pessoa('Thais', '15/08/1985')
    p2.quant_filhos = 3
    print(p2.cumprimentar())
    print(p2.__dict__)
    p3 = Pessoa('Thaylor', '07/02/2003')
    print(p3.cumprimentar())
    print(p3.__dict__)
    p4 = Pessoa('Tayler', '05/08/2006')
    print(p4.cumprimentar())
    print(p4.__dict__)
    p5 = Pessoa('Theodora', '07/10/2019')
    print(p5.cumprimentar())
    print(p5.__dict__)
    print(Pessoa.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())