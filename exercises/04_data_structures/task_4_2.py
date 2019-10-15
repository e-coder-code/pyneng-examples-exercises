# -*- coding: utf-8 -*-
import re
'''
Задание 4.2

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
replacement = lambda string: string.replace(':', '.')
print(replacement(mac))

match = re.sub(':', '.', mac)
print(match)

