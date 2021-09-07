const files = require('./files')

const applyColor = (txt, reg, color) => txt.replace(reg, `<span style="color: #${color}"><b>$1</b></span>`)

const text = files.read('source.html')

const codeRegex = /<code>[\s\S]*<\/code>/i
let code = text.match(codeRegex)[0]

//String
code = applyColor(code, /(\".*\")/g, 'ce9178')

//reserved words
code = applyColor(code, /\b(package|public|class|static|if|else)\b/g, 'd857cf')

//types
code = applyColor(code, /\b(void|int)\b/g, '1385e2')

//multiline comment
code = applyColor(code, /(\/\*[\s\S]*\*\/)/g, '267703')

//one line comment
code = applyColor(code, /(\/\/.*?\n)/g, '267703')

const finalContent = text.replace(codeRegex, code)

files.write('source.html', finalContent)
