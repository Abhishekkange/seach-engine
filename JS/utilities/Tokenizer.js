const tokenize = (text)=>{

    return  text.toLowerCase().split(/\W+/).filter(word => word.trim() !== '');

}

module.exports = tokenizer;