# -*- coding: utf-8 -*-
import re
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
pro, pre, ad, _, n_hop, l_up, intf = ospf_route.split()

print(
f"""
Protocol:              {pro}SPF
Prefix:                {pre}
AD/Metric:             {ad.strip('[]')}
Next-Hop:              {n_hop.rstrip(',')}
Last update:           {l_up.rstrip(',')}
Outbound Interface:    {intf}
"""
)

ospf_template = """
Protocol:              {}SPF
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
"""
ospf = re.split(r'(?:via|[ ,\[\]])+', ospf_route)

print(ospf_template.format(*ospf))

