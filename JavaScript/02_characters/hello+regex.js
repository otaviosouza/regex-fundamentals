const text = 'Casa bonita é a casa amarela da esquina com a Rua ACASALAR.'

const regex = /casa/gi

console.log(text.match(regex)) // [ 'Casa', 'casa', 'CASA' ]
console.log(text.match(/a b/g)) // [ 'a b' ]
console.log(text.match(/a b/gi)) // [ 'a b' ]