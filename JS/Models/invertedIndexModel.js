const mongoose = require('mongoose');

// Define the schema for the inverted index
const invertedIndexSchema = new mongoose.Schema({
    term: { type: String, required: true }, // The indexed term
    postings: [
        {
            product_ids: [{ type: String, required: true }], // Document ID
            positions: [{ type: Number, required: true }], // Positions of the term in the document
            frequency: { type: Number, required: true } // Frequency of the term in the document
        }
    ]
});

// Compile the schema into a model
const InvertedIndex = mongoose.model('InvertedIndex', invertedIndexSchema);

// Export the model
module.exports = InvertedIndex;
