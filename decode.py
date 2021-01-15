# NRZI код (Non Return to Zero Invertive) — один из способов
# линейного кодирования. Обладает двумя уровнями сигнала и
# используется для передачи битовых последовательностей, содержащих
# только 0 и 1. NRZI применяется, например, в оптических кабелях,
# где устойчиво распознаются только два состояния сигнала — свет
# и темнота.
#
# Принцип кодирования
# При передаче логического нуля на вход кодирующего устройства
# передается потенциал, установленный на предыдущем такте
# (то есть состояние потенциала не меняется), а при передаче
# логической единицы потенциал инвертируется на противоположный.
#
# Реализуйте функцию decode, которая принимает cтроку в виде
# графического представления линейного сигнала и возвращает
# строку с бинарным кодом.
#
# Примеры использования:
# >>> decode('_|¯|____|¯|__|¯¯¯')
# '011000110100'
# >>> decode('|¯|___|¯¯¯¯¯|___|¯|_|¯')
# '110010000100111'
# >>> decode('¯|___|¯¯¯¯¯|___|¯|_|¯')
# '010010000100111'
def decode(string):
    if not string:
        return ''
    result = ''
    list_len = list(map(len, string.split('|')))
    if string[0] != '|':
        result = '{}'.format('0' * list_len[0])
    return '{a}{b}'.format(
        a=result, b=''.join(
            list(
                map(
                    lambda x: ('1{a}'.format(a=(x - 1) * '0')), list_len[1:],
                )
            )
        )
    )


if __name__ == '__main__':
    assert decode('') == ''
    assert decode('|¯') == '1'
    assert decode('_') == '0'
    assert decode('_|¯|____|¯|__|¯¯¯') == '011000110100'
    assert decode('|¯|___|¯¯¯¯¯|___|¯|_|¯') == '110010000100111'
    assert decode('¯|___|¯¯¯¯¯|___|¯|_|¯') == '010010000100111'
