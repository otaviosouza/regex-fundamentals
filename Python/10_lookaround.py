#!/usr/bin/env python
import re
from pprint import pp, pprint
"""
Lookaround -> Lookahead and Lookbehind
Zero-length assertions just like the beginning and end of line, and beginning and end of word anchors. The difference is that lookaround actually matches characters, but then gives up the match, returning only the result: match or no match.
"""


text = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# # Positive lookahead -> (?=...)
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', text))

# # Negative lookahead -> (?!...)
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', text))

# Positive lookbehind -> (?<=...)
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', text))

# Negative lookbehind -> (?<=...)
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', text))

