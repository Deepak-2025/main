<?php
 $showalert = false;
 $passalert = false;
if($_SERVER["REQUEST_METHOD"] == "POST"){
        
 include 'partials/db.php';
   
$name = $_POST['name'];
$password = $_POST['pass'];

$sql = "SELECT * FROM $database WHERE name ='$name'";

$result = mysqli_query($conn, $sql);
$num = mysqli_num_rows($result);

if($num == 1){
    while($row = mysqli_fetch_assoc($result)){
     if(password_verify($password, $row['password'])){
    $login = true;
    session_start();
    $_SESSION['loggedin'] = true;
    $_SESSION['name'] = $name;
    header("location: welcome.php");
    }
    else{
        $showalert = true;
        $_SESSION['loggedin'] = false;
        $login = false;
       
    }
    }
}
else{
    $showalert = true;
    $_SESSION['loggedin'] = false;
    $login = false;
   
}
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
            <a href="login.php">LOGIN</a>
            <a href="signup.php">SIGNUP</a>
            <a href="about.php">ABOUT</a>
            <input type="text" placeholder="search">
        </nav>
        <?php
        if($showalert == true){
            echo '<div class="nav">
            <p><b>warning: </b> your username or password is not valid. </p>
        </div>';
        }
        ?>

    <div class="container">
        <div class="form">
            <form action="login.php" method="post">
                <h2>LOGIN TO ERA</h2>

                <p><b> username</b></p>

                <input type="text" maxlength="20" name="name" placeholder="enter your name" required>

                <p><b> password</b></p>

                <input type="password" maxlength="25" name="pass" placeholder="enter your password " required> <br>

                <button type="submit" name="submit">LOGIN</button>
                
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
        padding: 20px;
    }
    .form form p{
        font-size: 18px;
        padding-right: 30px;
        margin-right: 90px;
        margin-bottom: 8px;
    }
    .form form h3{
        font-size: 16px;
        margin-right: 65px;
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
        
        
    }
    .form button{
        background-color: chocolate;
        color: antiquewhite;
        padding: 8px 20px;
        border: 8px;
        border-radius: 10px;
        border-color: black;
        margin-top: 10px;
        margin-right: 125px;
    }
    .nav{
        background-color: rgb(202, 37, 16);
        color: aliceblue;
        padding: 1px 5px;
        font-size: 15px;
        border-radius: 8px;
    }
    .nav p{
        background-color: rgb(202, 37, 16);
        color: aliceblue;
    }
    .nav p b{
        background-color: rgb(202, 37, 16);
        color: aliceblue;
    }
</style>
</html>