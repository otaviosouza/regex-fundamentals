#!/usr/bin/env python
import re

"""
Greedy : consume as much of the pattern as possible.
* , + , ?

Non-greedy (lazy) : match as little of the pattern as possible.
*? , +? , ??, { }?

"""

text = '''
<p>Paragraph 1</p> <p>Paragraph 2</p> <p>Paragraph 3</p> <div>Not a paragraph, but a div</div> <div></div>
'''

# Greedy
print('{}'.format(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', text)))

# Non-greedy
print('{}'.format(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', text)))
print('{}'.format(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', text))) # without the empty div
