<?php
// for connect to the db
$servername  = "localhost";
$username  = "root";
$password  = "";
$name = $_POST['name'];
//in $database enter name of your db
     //change
$database = $name;

//create a connection
$conn = mysqli_connect($servername,$username,$password);

//die if connection was not successful
if(!$conn){
    die ("sorry database connection was failed" . mysqli_connect_error());
    echo "<br>";
    }
    else{
    echo "<br>";
    }

$sql = "CREATE DATABASE $database";

$result = mysqli_query($conn, $sql);

// for check the connection
if($result){
     echo "<script> alert ('database created') </script>";
    echo "<br>";
}
else{
echo "the table was not created or created already"."<br>".mysqli_error($conn);
echo "<br>";
}
?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>creating database</title>
</head>
<body>
<div class="container">
    <h3><b> please enter db name:</b></h3> <br>
        <div class="db">
         <form action = "create.php" method="post">
            <input type="text" name="name" placeholder = "ENTER DB NAME" style="background-color: white;" ><br><br>
            <input type="submit" name="submit"  >
            <h5><?php 
            echo "database : ('$name') CREATED";
            ?></h5>
         </form>
       </div>
</body>
</div>
<style>
    * {
        text-align: center;
        background-color: #f5f0e1;
        color: #1e3d59;
    }

    .container {
        padding: 5px;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
    }
    .db{
        text-align: center;
        background-color: #587e76;
        padding: 20px;
        border-radius: 8px;
    }

    .db h5{
        color: white;
        background-color: #587e76; 
    }

    .db form{
        background-color: #587e76;
     
    }
    .db form input{
        color: black;
        text-decoration: none;
        border-color:#ff6e40;
        border-radius:8px;
        padding: 7px 18px;
        background-color: #ff6e40;
    }
    
</style>
</html>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>table creating</title>
</head>

<body>
    <div class="container">
        <div class="form">
            <form action="collect.php" method="post">
              
            <p> ENTER VALUES FOR CREATE TABLES :</p>

               <input type="text" name="name" placeholder="please enter db name" value="<?php echo $name;?>"><br><br>

                <input type="text" name="column1" placeholder = "column1"><br>
                <input type="text" name="column2" placeholder = "column2"><br>
                <input type="text" name="column3" placeholder = "column3"><br>
                <input type="text" name="column4" placeholder = "column4"><br><br>
                <input type="submit" name="submit" style="color: rgb(0, 0, 0);" style="background-color: #40ff4a;">
            </form>
        </div>
        <div class="next">
       
        </div>
    </div>
    <h3>NOTE- 1.for more column you have to change the code <br>
              2.sn. already created
    </h3>
</body>
<style>
    body {
        background-color: #f5f0e1;
        padding: 0;
        margin: 0;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        text-align: center;
    }

    #header {
        background-color: black;
        color: #fff;
        padding: 5px;
    }
    table{
      
        padding-left: 35%;
        padding-top: 40px;
    }
    tr{
        border-color:black;
      
    }
    th,
    td {
        padding: 15px;
        color: white;
        background-color: #587e76;
        border-color:black;
        text-align: left;
    }
    .form input{
        color: black;
        text-decoration: none;
        border-color:#ff6e40;
        border-radius:8px;
        padding: 7px 15px;
        background-color: white;
    }
    .container form {
        color: rgb(0, 0, 0);
        font-size: 25px;
    }
    .container form button {
        padding: 8px 30px;
        font-size: 20px;
        background-color: #ff6e40;
        border-radius: 10px;
        border-color: #ff6e40;
        color: white;
        text-decoration: none;
    }
    .container form p{
        padding-bottom: 5px;
        padding-top: 1px;
       
    }
</style>
</html>


