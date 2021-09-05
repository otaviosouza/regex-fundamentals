// period does not match \n

const text = 'Good\nmorning'

console.log(text.match(/.../gi)) // [ 'Goo', 'mor', 'nin' ]
console.log(text.match(/..../gi)) // [ 'Good', 'morn' ]