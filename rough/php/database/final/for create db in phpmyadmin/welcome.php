<?php
session_start();

if($_SESSION['loggedin'] == false){
    header("location: login.php");
exit;
}

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>login</title>
</head>
<body>
        <nav>
            <a href="welcome.php">HOME</a>
            <a href="logout.php"> LOGOUT </a> 
            <a href="about.php">ABOUT</a>
            <input type="text" placeholder="search">
        </nav>

    <div class="p">
       <p>welcome - '<?php echo $_SESSION['name'];?>' <br>  <p1>Lorem ipsum dolor, sit amet consectetur adipisicing elit. <br>Quam mollitia magnam earum repudiandae corrupti iure et! Necessitatibus nobis quasi sunt nostrum. <br>Deleniti sapiente dolore doloremque, fugit officiis tempore, dolores similique molestiae ea odit accusantium eligendi unde optio, impedit <br>consectetur. Nemo adipisci fugit minus sapiente <br>fugiat consequatur officia explicabo doloribus nisi.</p1></p><br>
      
    </div>
</body>
<style>
    *{
        background-color: #f5f0e1;
        color: #1e3d59;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        text-align: center;
    }
    .p{
        margin-top: 20vh;
        color: white;
        padding: 10px 20%;
    }
    .p p{
        background-color: green;
        color: white;
        font-style: bold;
        font-size: 25px;
        border-radius: 8px;
        padding: 8px;
    }
    .p p1{
        background-color: green;
        color: white;
        font-size: 15px;
    }
    nav{
        font-size: 20px;
       border-radius: 8px;
        word-spacing: 4px;
        background-color: rgb(19, 82, 124);
        padding: 10px;
    }
    nav a{
        font-size: 18px;
        text-decoration: none;
        background-color: rgb(19, 82, 124);
        color: #fff;
        border-radius: 8px;
        padding: 8px 15px;   
        text-align: left;
       
    }
    nav input{
        padding: 8px 30px;
        text-decoration: none;
        border-radius: 8px;
        border-color: black;
        margin-left: 45vw; 
    }
 
</style>
</html>