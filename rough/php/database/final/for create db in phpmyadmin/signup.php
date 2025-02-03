<?php
 $green = false;
 $red = false;
if($_SERVER["REQUEST_METHOD"] == "POST")
{        
include 'partials/db.php';
   
$name = $_POST["name"];
$password = $_POST["pass"];
$repassword = $_POST["repass"];

$exsql = "SELECT * FROM $database WHERE name = '$name'";

$result = mysqli_query($conn, $exsql);

$row = mysqli_num_rows($result);

 if($row > 0 ){
   $red = "this username is already exist.";
 }
 else{
    if($password == $repassword){  
    $hash = password_hash($password, PASSWORD_DEFAULT);
    $sql = "INSERT INTO $database (`SN.`, `name`, `password`, `date`) VALUES (NULL, '$name', '$hash', current_timestamp())";
    $result = mysqli_query($conn, $sql);

        if($result){
        $green = "your account is created successfully. now  you can login to your account." ;
                  }
                               }
        if($password != $repassword){
        $red =  "your passwords does not match."; 
                                    }
    }
}
?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>signup</title>
</head>
<body>
        <nav>
            <a href="welcome.php">HOME</a>
            <a href="login.php">LOGIN</a>
            <a href="signup.php">SIGNUP</a>
            <a href="about.php">ABOUT</a>
            <input type="text" placeholder="search">
        </nav>

        <?php
        if($green){
            echo '<div class="nav">
            <p><b>signup done: </b> '. $green .' </p>
        </div>';
        }
        ?>
         <?php
         if( $red){
                    echo '<div class="na">
                    <p><b>warning: </b> '. $red .' </p>
                </div>';
                }
         ?>

    <div class="container">
        <div class="form">
            <form action="signup.php" method="POST">
                <h2>SIGNUP FOR EGA</h2>

                <p><b> username</b></p>

                <input type="text" maxlength = "20" name="name" placeholder="enter your name" required>

                <p><b> password</b></p>

                <input type="password" maxlength = "25" name="pass" placeholder="enter your password " required>

                <h3><b> confirm password</b></h3>

                <input type="password" maxlength = "25" name="repass" placeholder="re-enter password" required> <br>
               
                <button type="submit" name="submit">SIGNUP</button>
                
            </form>
        </div>
    </div>
</body>
<style>
    *{
        background-color: #f5f0e1;
        color: #1e3d59;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
    }
    nav{
        font-size: 20px;
       border-radius: 8px;
        word-spacing: 7px;
       
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
        margin-left: 5px;
       
    }
    nav input{
        padding: 8px 28px;
        text-decoration: none;
        border-radius: 8px;
        border-color: black;
        margin-left: 45vw; 
    }
    .container{
        padding: 40px;
    }
    .form{
        text-align: center;

    }
    .form form h2{
        text-align: center;
        padding: 10px;
        font-size: 20px;
        word-spacing: 2px;
        letter-spacing: 5px;
    }
    .form form p{
        font-size: 15px;
        padding-right: 30px;
        margin-right: 150px;
        margin-bottom: 8px;
    }
    .form form h3{
        font-size: 14px;
        margin-right: 130px;
        margin-top: 10px;
        margin-bottom: 8px;
        margin-top: 15px;
    }
    .form form input{
        text-decoration: none;
        padding: 8px 20px;
        border-color: black;
        border-radius: 10px;
        margin-bottom: 10px;
        padding-right: 70px;
        
        
    }
    .form button{
        background-color: chocolate;
        color: antiquewhite;
        padding: 10px 20px;
        border: 8px;
        border-radius: 10px;
        border-color: black;
        margin-top: 10px;
        margin-right: 170px;
    }
    .nav{
        background-color: rgb(52, 146, 23);
        color: aliceblue;
        padding: 1px 5px;
        font-size: 15px;
        border-radius: 8px;
    }
    .nav p{
        background-color: rgb(52, 146, 23);
        color: aliceblue;
    }
    .nav p b{
        background-color: rgb(52, 146, 23);
        color: aliceblue;
    }
    .na{
        background-color: rgb(202, 37, 16);
        color: aliceblue;
        padding: 1px 5px;
        font-size: 15px;
        border-radius: 8px;
    }
    .na p{
        background-color: rgb(202, 37, 16);
        color: aliceblue;
    }
    .na p b{
        background-color: rgb(202, 37, 16);
        color: aliceblue;
    }
 
</style>
</html>