#!/usr/bin/env python
import re

"""
re.A -> ASCII
re.I -> IGNORECASE
re.M -> Multiline -> ^...$
re.S -> DotAll
"""



text = '''
197.124.690-50
    965.983.940-58
268.118.380-43
- 487.506.180-32
888.471.660-80
'''
text2 = 'Mollit sit aute eiusmod minim\nexcepteur cupidatat duis anim'

print('# Multiline')
print('{}'.format(re.findall(r'\d{3}\.\d{3}\.\d{3}-\d{2}', text)))
print('{}'.format(re.findall(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', text)))
print('{}'.format(re.findall(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', text, flags=re.M)))

print('\n# DotAll')
print('{}'.format(re.findall(r'^m.*m$', text2, flags=re.I)))
print('{}'.format(re.findall(r'^m.*m$', text2, flags=re.I | re.S)))
