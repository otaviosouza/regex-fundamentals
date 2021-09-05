const text = 'a   b'

console.log(text.match(/a   b/g))
console.log(text.match(/a\s\s\sb/g))
console.log(text.match(/a...b/g))

// using quantifiers
console.log(text.match(/a\s+b/g))
console.log(text.match(/a {3}b/g))
console.log(text.match(/a\s{3}b/g))