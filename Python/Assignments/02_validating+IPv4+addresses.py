#!/usr/bin/env python
import re

# re.X -> verbose (accept comment)
# numbers 0-255
# ip_regex = re.compile(
#     r'''
#     ^(?:
#         (?:
#             \d{1,2}|    # 1-99
#             1\d{2}|     # 100-199
#             2[0-4]\d|   # 200-249 
#             25[0-5]     # 250-255
#         )\.?
#     ){4}\b$
#     ''', flags=re.X)

ip_regex = re.compile(r'^\b(?:(?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.?){4}\b$')

for i in range(291):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_regex.findall(ip))