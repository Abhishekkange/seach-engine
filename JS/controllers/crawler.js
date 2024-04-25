// Importing using CommonJS syntax
const { connectToStore, getCollection } = require("../Db/storesDb");
const Tokenizer = require('../utilities/Tokenizer');


async function crawlProduct (req,res){

    //fetch id of product to be crawled and database
    const id = req.body.id;
    const storeId = req.body.storeId;

    const Product = await getCollection(storeId,'product');

    //get the product to be indexed
    const productData = await Product.find({_id:id});

    return res.json({productData});
    
}

async function indexProduct(req,res)
{

    //fetch the product data to be indexed
    const productData = req.body.productData;

    //index Title 
    const titleTokens = Tokenizer.Tokenizer(productData.title);
    console.log(titleTokens);



}




module.exports = {crawlProduct,indexProduct}