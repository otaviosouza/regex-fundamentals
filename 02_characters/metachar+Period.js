// . - match any one character

const text = '0,1,2,3,4,5,6,7,8,9'
console.log(text.match(/1.2/g)) // any one character between 1 and 2
console.log(text.match(/1..2/g)) // any two characters between 1 and 2

const grades = '8.3, 7.1, 8.8, 10.0'
console.log(grades.match(/8../g)) // [ '8.3', '8.8' ]
console.log(grades.match(/.\../g)) //  '8.3', '7.1', '8.8', '0.0' ]