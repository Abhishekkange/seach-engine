const express = require('express');
const app = express();
const PORT = process.env.PORT || 4200

const crawler = require('./Routers/crawler');

app.use(express.json());

app.use('/crawler',crawler);





app.listen(PORT,()=>{

    console.log('search service listening on port : '+PORT);

})