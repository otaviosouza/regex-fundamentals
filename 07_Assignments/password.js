const password = `
123456
cod3r
QUASE123!
#OpA1
#essaSenhaEGrande1234
#OpA1?
Foi123!`

// base
console.log(password.match(/^.{6-20}$/gm))
console.log(password.match(/^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%!^&*]).{6-20}$/gm))
