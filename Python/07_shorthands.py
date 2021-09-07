#!/usr/bin/env python
import re

"""
\w -> any alphanumeric character -> [a-zA-Z0-9À-ú_]
\w -> flags=re.A -> [a-zA-Z0-9_]

\W -> any non-alphanumeric character -> [^a-zA-Z0-9À-ú_]

\d -> any decimal digit -> [0-9]
\D -> [^0-9]

\s -> any whitespace -> [ \t\n\r\f\v]
\S -> [^ \t\n\r\f\v]

\b -> matches the empty string, but only at the beginning or end of a word
\B -> matches the empty string, but only when it is not at the beginning or end of a word
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

print('{}'.format(re.findall(r'[0-9A-Za-z]+', text))) # only ASCII characters

print('{}'.format(re.findall(r'\w+', text)))
print('{}'.format(re.findall(r'\w+', text, flags=re.A)))

# boundaries
print('{}'.format(re.findall(r'\be\w+', text))) # all words beginning on 'e'
print('{}'.format(re.findall(r'\w+e\b', text))) # all words ending on 'e'
print('{}'.format(re.findall(r'\b\w{4}\b', text))) # all words with 4 characters
print('{}'.format(re.findall(r'\w{4}', text))) # split all words in 4 characters

text1 = 'ExcElEnte EsquEce'
print('{}'.format(re.findall(r'e\b', text1, flags=re.I)))
print('{}'.format(re.findall(r'e\B', text1, flags=re.I)))
