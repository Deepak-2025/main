*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'poppins',sans-serif;
}

body{
    display: flex;
    height: 100vh;
    justify-content: center;
    align-items: center;
    padding: 10px;
    background: linear-gradient(135deg,#2c3e50,#4ca1af);
}
.container{
    max-width: 700px;
    width: 100%;
    background: #fff;
    padding: 25px 30px;
    border-radius: 5px;
}
.container .title{
    font-size: 25px;
    font-weight: 500;
    position: relative;
}
.container .title::before{
    content: '';
    position: absolute;
    left: 0;
    bottom: 0;
    height: 3px;
    width: 30px;
    background: linear-gradient(135deg,#2c3e50,#4ca1af);
}
.container form .user-details{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
form .user-details .input-box{
    margin: 15px 0 12px 0;
    width: calc(100% / 2 - 20px);
}
.user-details .input-box .details{
    display: block;
    font-weight: 500;
    margin-bottom: 5px;
}
form .user-details .input-box input{
    height: 45px;
    width: 100%;
    outline: none;
    border-radius: 5px;
    border: 1px solid #ccc;
    padding-left: 15px;
    font-size: 16px;
    border-bottom-width: 2px;
transition: all 0.3s ease;
}
.user-details .input-box input:focus,
.user-details .input-box input:valid{
    border-color: #0768bd96;
}
form input[type="radio"]{
    display: none;
}
form .button{
    height: 40px;
    margin: 40px 0;
}
form .button input{
    height: 100%;
    width: 100%;
    outline: none;
    color: #fff;
    border: none;
    font-size: 20px;
    font-weight: 500;
    border-radius: 5px;
    letter-spacing: 1px;
    background: linear-gradient(135deg,#2c3e50,#4ca1af);
}
form .button input:hover{
    background: linear-gradient(-135deg,#2c3e50,#4ca1af);
}
@media(max-width: 574px){
    .container{
        max-width: 90%;
        height: 500px;
    }
    form .user-details .input-box{
        margin-bottom: 0px;
        width: 95%;
    }
    .container form .user-details{
        max-width: 300px;
        overflow-y: scroll;
        height: 350px;
      
    }
    .user-details::-webkit-scrollbar{
        width: 30;
    }
}