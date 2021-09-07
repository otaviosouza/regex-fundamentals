#!/usr/bin/env python
import re

cpf_regex = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

cpf_list = [
'197.124.690-50',
    '   965.983.940-58',
'268.118.380-43',
'- 487.506.180-32',
'888.471.660-80'
]

print('{}'.format(cpf_regex.search(cpf_list[0])))
print('{}'.format(cpf_regex.search(cpf_list[1])))
print('{}'.format(cpf_regex.search(cpf_list[3])))
