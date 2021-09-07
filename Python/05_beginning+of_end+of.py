#!/usr/bin/env python
import re

"""
Metacharacters
^ -> beginning of it
$ -> end of it
[^ ] -> any character NOT between the brackets
"""

cpf = 'a888.471.660-80 anything'
cpf1 = '888.471.660-80 anything'

print('{}'.format(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf)))
print('{}'.format(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))) # empty
print('{}'.format(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf1)))
print('{}'.format(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf1))) # empty

print('{}'.format(re.findall(r'[^A-z.-]+', cpf)))
print('{}'.format(re.findall(r'[^A-z.-]+', cpf1)))