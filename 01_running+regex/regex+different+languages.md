# Running RegEx on different languages

## JavaScript

```javascript
const text = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, e, f'

const regexNine = RegExp('9')
console.log('RegExp methods')
console.log(regexNine.test(text)) // Output: true
console.log(regexNine.exec(text)) // Output: ['9', index: ##, input:]

const regexChar = /[a-f]/g
console.log('String methods')
console.log(text.match(regexChar)) // Output: ['a', 'b', 'c', 'e', 'f']
console.log(text.search(regexChar)) // Output: first element of the RegEx
console.log(text.replace(regexChar, '*'))
console.log(text.split(regexChar))
```

## Python

```python
#!/usr/bin/env python

import re

text = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f'

patternNine = re.compile('9')

matchOne = re.search(patternNine, text)

print("Positions: %s, %s; Value: %s." %(matchOne.start(), matchOne.end(), matchOne.group(0))) #Positions: 27, 28; Value: 9.

values = re.findall('[a-f]', text)

print("Values: %s" %values) # Values: ['a', 'b', 'c', 'd', 'e', 'f']
```

## Ruby

```ruby
text = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f'

regexNine = Regexp::new('9')
puts 'RegExp methods'
puts regexNine.match(text) # Output: 9

regexNine = %r{9}
puts regexNine.match(text) # Output: 9

p regexNine =~ '894' # Output: 1 - true

regexChar = /[a-f]/
puts text.scan(regexChar).join() # Output: abcdef
puts text.split(/,/).join(' ') # Output: 0 1 2 3 4 5 6 7 8 9 a b c d e f

print text.split(/[aeiou]/) # Output: ["0, 1, 2, 3, 4, 5, 6, 7, 8, 9,", ", b, c, d,", ", f"]
```