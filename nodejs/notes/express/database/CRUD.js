const express = require("express")
const app = express()
const connection = require('./connection')

// app.get('/',(req,res)=> {
    
//     res.send("hello")
// })

app.get('/create',async (req,res)=> {
   let create =  await connection.create({
        name:"rohan",
        email:"rohan@gmail.com",
        username:"rohan123"
    })
    res.send(create)
})
app.get('/find',async (req,res)=> {
   let find =  await connection.find()
    res.send(find)
})
app.get('/update',async (req,res)=> {
   let update =  await connection.findOneAndUpdate(
    {name:"rahul"},
    {name:"sohan"},
    {new:true}
   )
    res.send(update)
})
app.get('/delete',async (req,res)=> {
   let delet =  await connection.findOneAndDelete(
    {name:"mohan"},
   )
    res.send(delet)
})

app.listen(3000)
