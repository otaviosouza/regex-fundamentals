const text = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f'

const regexNine = RegExp('9')
console.log('RegExp methods')
console.log(regexNine.test(text)) // Output: true
console.log(regexNine.exec(text)) // Output: ['9', index: ##, input:]

const regexChar = /[a-f]/g
console.log('String methods')
console.log(text.match(regexChar)) // Output: ['a', 'b', 'c', 'd', 'e', 'f']
console.log(text.search(regexChar)) // Output: first element of the RegEx
console.log(text.replace(regexChar, '*'))
console.log(text.split(regexChar))