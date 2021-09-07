#!/usr/bin/env python
import re

"""
Metacharacters: characters that don’t match themselves.
Instead, they signal that some out-of-the-ordinary thing should be matched, or they affect other portions of the RE by repeating them or changing their meaning.

. ^ $ * + ? { } [ ] \ | ( )
"""

text = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970.
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# | (alternation or "or" operator) : find any of the specified alternatives
# follows appearance order
print('{}'.format(re.findall(r'João|Maria|adultos', text)))

# [] : specifies a character class
# find any character inside the brackets
regex_or = re.findall(r'João|joão|Maria|maria|adultos', text)
regex_class = re.findall(r'[Jj]oão|[Mm]aria|adultos', text)

print('{}'.format(regex_or == regex_class))

# [A-Za-z] range : matches a single or none of character between A and z on ASCII table
print('{}'.format(re.findall(r'[A-Za-z]oão|[A-Za-z]aria', text)))

# ignore case
print('{}'.format(re.findall(r'jOãO|mAriA', text, flags=re.I)))