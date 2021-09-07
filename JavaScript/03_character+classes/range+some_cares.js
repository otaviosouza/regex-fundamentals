const text = 'ABC [abc] a-c 1234'

console.log(text.match(/[a-c]/g))
console.log(text.match(/a-c/g)) // does not define a range

console.log(text.match(/[A-z]/g)) // range meets UNICODE table order
// console.log(text.match(/[a-Z]/g)) // range out of order UNICODE table starts by capital letters
// console.log(text.match(/[4-1]/g)) // range out of order
console.log(text.match(/[a-zA-Z]/g)) // only letters