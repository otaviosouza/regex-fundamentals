// 8 bits: 256 characters - symbols, A-Z, a-z, 0-9
// 16 bits: 65500+ characters - symbols, A-Z, a-z, 0-9
// unicode: 1M+ characters

const text = 'aʬc௵d'

console.log(text.match(/\u02AC|\u0BF5/g))