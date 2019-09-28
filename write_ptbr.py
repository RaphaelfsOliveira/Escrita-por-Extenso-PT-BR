# "utf-8"


class WriteOutPTBR(object):

    def __init__(self):
        self.unity = {
            0: '', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro',
            5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito',9: 'nove'
        }

        self.ten = {
            0: '',
            1: {
                0: 'dez', 1: 'onze', 2: 'doze', 3: 'treze', 4: 'catorze', 5: 'quinze',
                6: 'desesseis', 7: 'desessete', 8: 'dezoito', 9: 'dezenove'
            },
            2: 'vinte', 3: 'trinta', 4: 'quarenta', 5: 'cinquenta',
            6: 'sessenta', 7: 'setenta', 8: 'oitenta', 9: 'noventa'
        }

        self.hundred = {
            0: '', 100: 'cem', 1: 'cento', 2: 'duzentos', 3: 'trezentos', 4: 'quatrocentos',
            5: 'quinhentos', 6: 'seiscentos', 7: 'setessentos', 8: 'oitocentos', 9: 'novecentos'
        }

        self.magnitude = {
            0: 'mil', 1: 'milhão', 2: 'milhões'
        }

    def make_unity(self, unity, ten=0):
        if int(ten) == 1:
            return ''
        return self.unity[int(unity)]

    def make_ten(self, ten, unity=0):
        if int(ten) == 1:
            return self.ten[int(ten)][int(unity)]
        return self.ten[int(ten)]

    def make_hundred(self, hundred):
        return self.hundred[int(hundred)]

    def make_unit_and_ten(self, numbers):
        if len(numbers) > 1 and int(numbers[0]) not in [0, 1] and int(numbers[1]) != 0:
            return '{} e {}'.format(self.make_ten(numbers[0], numbers[1]),
                                    self.make_unity(ten=numbers[0], unity=numbers[1]))
        elif len(numbers) == 1:
            return '{}'.format(self.make_ten(numbers))
        else:
            return '{}{}'.format(self.make_ten(numbers[0], numbers[1]),
                                 self.make_unity(ten=numbers[0], unity=numbers[1]))

    def make_unit_ten_hundred(self, integers):
        CEM = 100
        length = int(len(integers))

        if length == 3:
            if int(integers) == CEM:
                return '{}'.format(self.hundred[CEM])
            if int(integers[1]) == 0 and int(integers[2]) == 0:
                return '{} {}'.format(self.make_hundred(integers[0]),
                                     self.make_unit_and_ten([integers[1], integers[2]]))

            return '{} e {}'.format(self.make_hundred(integers[0]),
                                    self.make_unit_and_ten([integers[1], integers[2]]))
        elif length == 2:
            return '{}'.format(self.make_unit_and_ten([integers[0], integers[1]]))
        elif length == 1:
            return '{}'.format(self.make_unity(unity=integers))

    def add_thousand(self, thousand):
        if int(thousand):
            return '{} {} '.format(self.make_unit_ten_hundred(thousand),
                                   self.magnitude[0])
        return ''

    def add_million(self, million, mag):
        magnitude = self.magnitude[2]
        if mag == 1 and len(million) == 1: magnitude = self.magnitude[1]

        return '{} {}'.format(self.make_unit_ten_hundred(million),
                              magnitude)

    def add_magnitude(self, integers):
        length = int(len(integers))
        
        if length <= 3:
            return '{}'.format(self.make_unit_ten_hundred(integers))

        if length <= 6:
            hundred = integers[length - 3: length]
            thousand = integers[0:length - 3]

            return '{} {}'.format(self.add_thousand(thousand),
                                  self.make_unit_ten_hundred(hundred))

        if length <= 9:
            hundred = integers[length - 3: length]
            thousand = integers[length - 6:length - 3]
            million = integers[0:length - 6]

            return '{} {} {}'.format(self.add_million(million, int(integers[length - 7])),
                                     self.add_thousand(thousand),
                                     self.make_unit_ten_hundred(hundred))

    def written_in_full(self, number):
        edit_number = str(number).split('.')

        if len(edit_number) > 1:
            integers = edit_number[0]
            decimals = edit_number[1]

            return '{}, {}'.format(self.add_magnitude(integers),
                                   self.make_unit_and_ten(decimals)).replace('   ', ' ')\
                                                                    .replace('  ', ' ')
        integers = edit_number[0]
        return '{}'.format(self.add_magnitude(integers)).replace('   ', ' ')\
                                                        .replace('  ', ' ')


if __name__ == '__main__':
    from random import randrange, uniform
    from write_ptbr import WriteOutPTBR
    w = WriteOutPTBR()

    # numbers = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    # numbers = [700009.02, 800009.02, 900009.02]
    numbers = range(0, 50)

    for number in numbers:
        number = round(uniform(0, 991955600.99), 2)

        print_out = '{:>120} {:<} {:<}'.format(w.written_in_full(number),
                                              ' --> ',
                                              number)
        print(print_out)
