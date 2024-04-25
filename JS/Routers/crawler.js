const express = require('express');
const Router = express.Router();
const crawlerController = require('../controllers/crawler');

Router.get('/crawler', crawlerController.crawlProduct);

Router.post('/indexer',crawlerController.indexProduct);

