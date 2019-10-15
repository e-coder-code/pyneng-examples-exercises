# -*- coding: utf-8 -*-
import re
'''
Задание 4.1

Обработать строку nat таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
replace_nat = lambda string: string.replace('Fast', 'Gigabit')
print(replace_nat(nat))

match = re.sub('Fast', 'Gigabit', nat)
print(match)

