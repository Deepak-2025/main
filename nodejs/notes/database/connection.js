const mongoose = require('mongoose')

//database link
mongoose.connect(`mongodb://localhost:27017/mongoose1`)

//schema for get the data
const UserSchema  = mongoose.Schema({
    name:String,
    username:String,
    email:String
})

//create model for database
//new is a collection name in mongodb (new=news)
module.exports = mongoose.model("new",UserSchema)