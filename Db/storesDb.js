const mongoose = require('mongoose');
require('dotenv').config();

const storeDBConnections = {};

const connectToStore = async (storeId) => {
    if (!storeDBConnections[storeId]) {
        try {
            const uri = process.env.MONGO_URL; // Fetch MongoDB connection URL from environment variable
            const connection = mongoose.createConnection(`${uri}/${storeId}`, {
                useNewUrlParser: true,
                useUnifiedTopology: true,
            });

            connection.on('error', (error) => {
                console.error(`Connection error for store ${storeId}: ${error}`);
            });

            connection.on('disconnected', () => {
                console.log(`Disconnected from store ${storeId}. Reconnecting...`);
            });

            storeDBConnections[storeId] = connection;

            return connection;
        } catch (error) {
            console.error(`Error connecting to store ${storeId}: ${error}`);
            throw new Error(`Error connecting to store ${storeId}`);
        }
    } else {
        return storeDBConnections[storeId];
    }
};

const createProductModel = (connection) => {
    const existingModel = connection.models['Product']; // Check if model exists for this connection
    if (existingModel) {
        return existingModel; // If the model exists, return it
    }

    const productSchema = new mongoose.Schema({
        name: {
            type: {
                en: String,
                hi: String,
                mr: String,
                // Add more languages if needed
            },
           
        },
        categories: [
            {
                categoryName: {
                    type: {
                        en: String,
                        hi: String,
                        mr: String,
                        // Add more languages if needed
                    }
                },
                categoryImage: String
            }
        ],
        subcategories: [
            {
                subcategoryName: {
                    type: {
                        en: String,
                        hi: String,
                        mr: String,
                        // Add more languages if needed
                    }
                },
                subcategoryImage: String
            }
        ],
        price: {
            type: Number,
            
        },
        shopName: {
            type: String,
           
        },
        shortDescription: {
            type: {
                en: String,
                hi: String,
                mr: String,
                // Add more languages if needed
            }
        },
        description: {
            type: {
                en: String,
                hi: String,
                mr: String,
                // Add more languages if needed
            }
        },
        reviews: [{
            comment: String,
            userId: String,
            timestamp: String,
            title: String,
        }],
        details: [{
            colors: [{
                colorName: String,
                colorCode: String,
                images: [{ Image: String }],
                sizes: [{
                    size: String,
                    qty: String
                }]
            }]
        }],
        image:String,
        barcodeNo: String,
        productScore:Number
    });
    
    return connection.model('Product', productSchema);
};

const createSubscriberListModel = (connection) => {
    const existingModel = connection.models['subscriberList']; // Check if model exists for this connection
    if (existingModel) {
        return existingModel; // If the model exists, return it
    }

    const subscriberListSchema = new mongoose.Schema({
        userId: String
    });

    return connection.model('subscriberList', subscriberListSchema);
}

const getCollection = async (storeId, collectionName) => {
    const connection = await connectToStore(storeId);
    if (connection.connected) {
        console.log(`Connected to ${storeId}`);
    }

    let Model;
    switch (collectionName) {
        case 'product':
            Model = createProductModel(connection);
            break;
        case 'subscriberList':
            Model = createSubscriberListModel(connection);
        default:
            // For other collections, if needed
            break;
    }

    return Model;
};

module.exports = { connectToStore, getCollection };
