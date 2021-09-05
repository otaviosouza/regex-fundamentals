#!/usr/bin/env python

import re

text = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f'

patternNine = re.compile('9')

matchOne = re.search(patternNine, text)

print("Positions: %s, %s; Value: %s." %(matchOne.start(), matchOne.end(), matchOne.group(0))) #Positions: 27, 28; Value: 9.

values = re.findall('[a-f]', text)

print("Values: %s" %values) # Values: ['a', 'b', 'c', 'd', 'e', 'f']