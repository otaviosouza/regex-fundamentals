#!/usr/bin/env python
import re
from pprint import pprint

"""
Grouping : allows to apply a quantifier to the entire group or to restrict alternation to part of the regex.
( )

Backreference : groups can be accessed as a variable. Backreferences allow to match the same content as previously matched by a capturing group.
( ) \1
( ) ( ) \1 \2
(( )) ( ) \1 \2 \3
"""

text = '''
<p>Paragraph 1</p> <p>Paragraph 2</p> <p>Paragraph 3</p> <div>Not a paragraph, but a div</div> <div></div>
'''

# print('{}'.format(re.findall(r'<([dpiv]{1,3})>.+?<\/\1>', text))) # ['p', 'p', 'p', 'div']

# \1 (<([dpiv]{1,3})>.+?<\/\2>)
# \2 ([dpiv]{1,3})
# \3 (.+?)
tags = re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)', text)
print('tags: {}'.format(tags)) # Output: list of tuples -> (\1, \2, \3)

tags1 = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', text)
print('tags1: {}'.format(tags1))

# ?: --> find content wrapped in tags but does not keep it
tags2 = re.findall(r'<([dpiv]{1,3})>(?:.+?)<\/\1>', text)
print('tags2: {}'.format(tags2))

# 1. does not keep \1 -> '<([dpiv]{1,3})>(.+?)<\/\1>'
# 2. \2 content '[dpiv]{1,3}' assumes as \1
tags3 = re.findall(r'(?:<([dpiv]{1,3})>(.+?)<\/\1>)', text)
print('tags3: {}'.format(tags3))

# pprint(tags)
# pprint(tags1)
# pprint(tags2)
# pprint(tags3)

print('tags == tags1: {}'.format(tags == tags1))
print('tags == tags2: {}'.format(tags == tags2))
print('tags == tags3: {}'.format(tags == tags3))

print('tags1 == tags2: {}'.format(tags1 == tags2))
print('tags1 == tags3: {}'.format(tags1 == tags3))
print('tags2 == tags3: {}'.format(tags2 == tags3))

# rebuild tags
print('{}'.format(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4', text)))

# for tag in tags:
#     grp_one, grp_two, grp_three = tag
#     print('{}'.format(grp_three))

# cpf = '888.471.660-80'
# print('{}'.format(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf)))
# print('{}'.format(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf)))

