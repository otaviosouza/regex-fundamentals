const text = '0 1 10 192 199 201 249 255 256 312 1010 1512'

const ipv4List = `
Not valid:
192.268.0.1
1.333.1.1
192.168.0.256
256.256.256.256

Valid:
192.168.0.1
127.0.0.1
10.0.0.255
10.11.12.0
255.255.255.255
0.0.0.0
`

const n = '(\\d{1,2}|1\\d{2}|2[0-4]\\d|25[0-5])'
const ipv4 = RegExp(`\\b${n}\\.${n}\\.${n}\\.${n}\\b`, 'g')

// numbers between 0-255
console.log(text.match(/\b(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\b/g))

console.log(ipv4List.match(ipv4))
