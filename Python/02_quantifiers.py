#!/usr/bin/env python
import re

"""
Quantifiers: are the minimum and maximum times the expression to which the quantifier applies must match.
It is applied to the expression on the left of the quantifier

* --> 0 or n
+ --> 1 or n
? --> 0 or 1
{ } --> min, max or n
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

# ignore case
print('{}'.format(re.findall(r'jo+ão+', text, flags=re.I)))

print('{}'.format(re.sub(r'jo*ão*', 'Felipe', text, flags=re.I)))
print('{}'.format(re.sub(r'jo?ão*', 'Felipe', text, flags=re.I)))

quant1 = re.findall(r'jo*ão*', text, flags=re.I)
quant2 = re.findall(r'jo{1,}ão{1,}', text, flags=re.I)
print('{}'.format(quant1 == quant2))
