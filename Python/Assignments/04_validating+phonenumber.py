#!/usr/bin/env python
import re

regexp = re.compile(r'^(?:\(\d{2}\)\s)(?:9\s)(?:\d{4}-\d{4})$', flags=re.M)

phone_list = '''
(21) 9 8852-5214
(11)9955-1231
(11)            9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
'''

for phone in regexp.findall(phone_list):
    print('{}'.format(phone))
