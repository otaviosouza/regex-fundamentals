const text1 = 'De longe eu avistei o fogo e uma pessoa gritando: FOGOOOOOO!'
const text2 = 'There is a big fog in NYC.'
const text3 = 'Numbers: 0123456789.'
const text4 = 'John won 120 million betting 6 9 21 23 45 46 on the lottery.'
const text5 = 'O João recebeu 120 milhões apostando 6 9 21 23 45 46 na loteria.'
const text6 = '<div>Content #01</div><div>Content #02</div>'



// ? -> one or none occurence of the char at left (optional)
console.log(text1.match(/fogo?/gi)) // [ 'fogo', 'FOGO' ]
console.log(text2.match(/fogo?/gi)) // [ 'fog' ]

// + -> one or more occurence of the char at left
console.log(text1.match(/fogo+/gi)) // [ 'fogo', 'FOGOOOOOO' ]
console.log(text2.match(/fogo+/gi)) // null

console.log(text3.match(/[0-9]/g)) // [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
console.log(text3.match(/[0-9]+/g)) // [ '0123456789' ]

// * -> none or more occurence of the char at left
console.log(text1.match(/fogo*/gi)) // [ 'fogo', 'FOGOOOOOO' ]
console.log(text2.match(/fogo*/gi)) // [ 'fog' ]

// {m, n} -> from m to n - more accurate range
console.log(text4.match(/\d{1,2}/g)) // [ '12', '0',  '6', '9',  '21', '23', '45', '46' ]
console.log(text4.match(/[0-9]{2}/g)) // [ '12', '21', '23', '45', '46' ]
console.log(text4.match(/\d{1,}/g)) // [ '120',  '6', '9',  '21', '23', '45', '46' ]

console.log(text4.match(/\w{7}/g)) // [ 'million', 'betting', 'lottery' ]
console.log(text5.match(/\w{7}/g)) // [ 'recebeu', 'apostan', 'loteria' ]
console.log(text5.match(/[\wõ]{7,}/g)) // [ 'recebeu', 'milhões', 'apostando', 'loteria' ]

// greedy
console.log(text6.match(/<div>.+<\/div>/g))
console.log(text6.match(/<div>.*<\/div>/g))
console.log(text6.match(/<div>.{0,100}<\/div>/g))

//lazy
console.log(text6.match(/<div>.+?<\/div>/g))
console.log(text6.match(/<div>.*?<\/div>/g))
console.log(text6.match(/<div>.{0,100}?<\/div>/g))
