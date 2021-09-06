const fs = require('fs')

const read = relativePath =>
    fs.readFileSync(`${__dirname}/original/${relativePath}`, { encoding: 'utf-8' })

const write = (fileName, content) => {
    const dirname = `${__dirname}/changed`
    if (!fs.existsSync(dirname)) {
        fs.mkdirSync(dirname)
    }
    fs.writeFileSync(`${dirname}/${fileName}`, content, { encoding: 'utf-8' })
}

module.exports = { read, write }
