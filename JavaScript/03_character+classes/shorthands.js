// \w - ASCII characters [a-zA-Z0-9_]
// \W - not characters [^a-zA-Z0-9_]
// \d - numbers [0-9]
// \D - not numbers [^0-9]
// \s - blanks [ \t\n\r\f]
// \S - not blanks [^ \t\n\r\f]

const text = `1,2,3,4,5,6,a.b c!d?e\r\f	-
f_g`

console.log(text.match(/\d/g))
console.log(text.match(/\D/g))
console.log(text.match(/\w/g))