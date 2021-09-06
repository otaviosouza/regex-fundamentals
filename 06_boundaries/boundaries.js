const text = 'Romário era um excelente jogador\n, mas hoje é um político questionador'

const multiline = `
    Leo é muito legal
    Emanuel foi jogar em Sergipe
    Bianca é casada com Habib
`

console.log(text.match(/r/gi))
console.log(text.match(/^r/gi))
console.log(text.match(/r$/gi))
console.log(text.match(/^r.*r$/gi)) // null --> period does not solve for \n (dotall issue)

// DotAll on JavaScript
console.log(text.match(/^r[\s\S]*r$/gi))

// multiline flag
console.log(multiline.match(/\n/g))
console.log(multiline.match(/^(\w).+\1$/gi))
console.log(multiline.match(/^(\w).+\1$/gim))

