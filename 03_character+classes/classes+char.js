// characters and sentences literally

const text = '1,2,3,4,5,6,a.b c!d?e[f'

const regexEven = /[02468]/g // used as OR

console.log(text.match(regexEven))

// with and without graphic accent

const word = 'João não passeará na moto'

const regexWord = /n[aã]/g

console.log(word.match(regexWord))

// range - borders are inclusive
console.log(text.match(/[a-z]/g))
console.log(text.match(/[b-d]/g))
console.log(text.match(/[2-4]/g))
console.log(text.match(/[A-Z1-3]/gi))
console.log(text.match(/[A-Za-z]/g))

// range and metacharacteres
const meta = '.?*+-^$:'

// may need a escape inside a class: - [] ^

console.log(meta.match(/[+.?*$]/g)); // do not need the escape inside a class
console.log(meta.match(/[+.?*$]./g)); // [ '.?', '*+', '$:' ]
console.log(meta.match(/[$-?]./g)); // range
console.log(meta.match(/[$\-?]./g)); // range
console.log(meta.match(/[-$?]./g)); // not a range

// denied range
console.log(text.match(/\D/g))
console.log(text.match(/[^0-9]/g))
console.log(text.match(/[^\d!\?\[\s,\.]/g))

// unicode range
const unicode = 'áéíóú àèìòù âêîôû ç ãõ ü'

console.log(unicode.match(/[À-ü]/g)) // UNICODE order