// get CPF
const cpf = `CPF dos aprovados:
    - 197.124.690-50
    - 965.983.940-58
    - 268.118.380-43
    - 487.506.180-32
`

console.log(cpf.match(/\d{3}\.\d{3}\.\d{3}-\d{2}/g))

// get phone number
const phoneNumber =`Phone list:
- (81) 91679-2786
- (88) 94190-7069
- 96053-0600
- (18) 90156-1057
- (29) 96452-2952
`
console.log(phoneNumber.match(/\(?\d{0,2}\)?\s?\d{4,5}-\d{4}/g))

// get email
const email = `Contact list:
    - eric.idle@monty.python
    - chapman@gmail.com
    - gilliam@monty.com.uk
    - john-cleese@hotmail.com
    - palin@monty.uk
`
//console.log(email.match(/\w+@\w+\.\w{2,}/gi))
console.log(email.match(/[\w.-]+@\w+\.\w{2,}/gi))