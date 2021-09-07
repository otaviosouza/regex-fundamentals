// . ? * + - ^ $ | [] {} () \ :

const text = '1,2,3,4,5,6,a.b c!d?e'

const regexPeriod = /\./g // find literally period
console.log(text.split(regexPeriod)) // [ '1,2,3,4,5,6,a', 'b c!d?e' ]

const regexSymbols = /,|\.|\?|!| /g
console.log(text.split(regexSymbols)) // ['1', '2', '3', '4', '5', '6', 'a', 'b', 'c', 'd', 'e']
