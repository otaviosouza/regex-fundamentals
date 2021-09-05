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