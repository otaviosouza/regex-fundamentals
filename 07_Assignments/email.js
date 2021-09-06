const email = `Contact list:
    - eric.idle@monty.python
    - chapman@gmail.com
    - gilliam@monty.com.uk
    - john-cleese@hotmail.com
    - palin@monty.uk
`

console.log(email.match(/\S+@\w+\.\w{2,6}(\.\w{2})?/g))