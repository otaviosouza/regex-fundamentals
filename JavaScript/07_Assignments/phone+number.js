// get phone number
const phoneNumber =`Phone list:
- (81) 91679-2786
- (88) 94190-7069
- 96053-0600
- (18) 90156-1057
- (29) 96452-2952
`
console.log(phoneNumber.match(/(\(\d{2}\)\s?)?\d{4,5}-\d{4}/g))