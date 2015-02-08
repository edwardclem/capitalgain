//schema validation for database
var stockSchema = new SimpleSchema({
    name: {
        type: String,
        label: "Name"
    },
    ticker: {
        type: String,
        label: "Ticker"
    },
    file: {
        type: String,
        label: "File Location"
    },
    musicdata: {
        type: [Object],
        label: "Music Data"
    }
});