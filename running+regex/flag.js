// g -global
// i - ignore case

const text = 'Eric signed the petition.'

console.log(text.match(/E|pe/)) //no flag
console.log(text.match(/e|pe/i)) // stop after found 1st occurrence
console.log(text.match(/e|pe/gi)) // continue after found 1st occurrence
console.log(text.match(/pe|e/gi))

