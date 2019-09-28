# "utf-8"


class WriteOutPTBR(object):

    def __init__(self):
        self.unity = {
            0: '', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
            6: 'seis', 7: 'sete', 8: 'oito',9: 'nove'
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
            0: '', 100: 'cem', 1: 'cento', 2: 'duzentos', 3: 'trezentos', 4: 'quatrocentos', 5: 'quinhentos',
            6: 'seiscentos', 7: 'setessentos', 8: 'oitocentos', 9: 'novecentos'
        }

        self.v = {
            'mil', 'milhão', 'milhões'
        }

    def make_unity(self, ten, unity):
        if int(ten) == 1:
            return ''
        return self.unity[int(unity)]

    def make_ten(self, ten, unity=0):
        if int(ten) == 1:
            return self.ten[int(ten)][int(unity)]
        return self.ten[int(ten)]

    def make_hundred(self, hundred):
        return self.hundred[int(hundred)]

    def make_decimals(self, decimals):
        if len(decimals) > 1 and int(decimals[0]) != 1:
            return '{} e {}'.format(
                self.make_ten(decimals[0], decimals[1]),
                self.make_unity(decimals[0], decimals[1])
            )
        elif len(decimals) == 1:
            return '{}'.format(self.make_ten(decimals))
        else:
            return '{}'.format(self.make_ten(decimals[0], decimals[1]))


    def make_integers(self, *args):
        pass

    def written_in_full(self, number):
        edit_number = str(number).split('.')

        integers = edit_number[0]
        decimals = edit_number[1]

        return '{} e {} e {}, {}'.format(
            self.make_hundred(integers[0]),
            self.make_ten(integers[1], integers[2]),
            self.make_unity(integers[1], integers[2]),
            self.make_decimals(decimals)
        )

if __name__ == '__main__':
    from write_ptbr import WriteOutPTBR
    w = WriteOutPTBR()

    unit = ['01', '02', '03', '04', '05', '06', '07', '08', '09']

    for n in unit:
        number = '200.{}'.format(n)
        # print(number, type(number), float(number))
        print(w.written_in_full(float(number)))
