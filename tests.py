if __name__ == '__main__':
    from random import randrange, uniform
    from write_ptbr import WriteOutPTBR
    w = WriteOutPTBR()

    # numbers = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    # numbers = [700009.02, 800009.02, 900009.02]
    numbers = range(0, 50)

    for number in numbers:
        number = round(uniform(0, 991955600.99), 2)

        # number = 1.00
        # number = 1000.54

        print_out = '{:>150} {:<} {:<}'.format(w.written_in_full(number),
                                              ' --> ',
                                              number)
        print(print_out)
