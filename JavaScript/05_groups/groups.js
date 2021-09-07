const text1 = 'José Simão is so funny... hahahaha'

const url = 'http://www.site.info www.escola.ninja.br google.com.ag'

const text2 = '<b>Title</b><strong>Subtitle</strong><div>Content</div>'
const text3 = 'Lentamente é mente muito lenta.'

const text4 = 'supermercado hipermercado minimercado mercado'

// ()
console.log(text1.match(/(ha)+/g))
console.log(url.match(/(http:\/\/)?(www\.)?\w+\.\w{2,}(\.\w{2})?/g))

// backreference
console.log(text2.match(/<(\w+)>.*<\/\1>/g))

console.log(text3.match(/(lenta)(mente).*\2.*\1\./gi))
console.log(text3.match(/(?:lenta)(mente).*\1/gi)) // ?: do not keep

console.log(text3.match(/(lenta)(mente)/gi))
console.log(text3.match(/(lenta)(mente)?/gi))
console.log(text3.replace(/(lenta)(mente)/gi, '$2'))

// nested
console.log(text4.match(/(super|hiper|mini)?mercado/g))
console.log(text4.match(/((su|hi)per|mini)?mercado/g))