# -*- coding: utf-8 -*-
import re
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
print(bin(int(mac.replace(':', ''), 16))[2:])
print(bin(int(re.sub(':', '', mac), 16))[2:])


