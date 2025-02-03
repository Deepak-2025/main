<?php
if(isset($_POST['submit'])){

//connect to the database
$servername  = "localhost";
$username  = "root";
$password  = "";

$database = //insert;

$conn = mysqli_connect($servername,$username,$password,$database);
if($conn){
  // echo "work";
}  

    $value1 = $_POST['value1'];
    $value2 = $_POST['value2'];
    $value3 =  $_POST['value3'];
    $value4 =  $_POST['value4'];
                                                //change this values
$sql = "INSERT INTO $database (`sn.`, `//insert`, `//insert`, `//insert`, `//insert`) VALUES (NULL,'$value1','$value2','$value3','$value4')";


if($sql){
   // echo "this work";
}
$result = mysqli_query($conn, $sql);
if($result){
    echo "<script> alert ('values inserted') </script>";
   // echo "insert";
}
else{
    echo"error";
}
//END
}
?>


