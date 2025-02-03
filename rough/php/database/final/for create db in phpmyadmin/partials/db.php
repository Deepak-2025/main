<?php

$server = "localhost";
$username = "root";
$password = "";
$database = 'logintoera';

$conn = mysqli_connect($server,$username,$password,$database);

if($conn){
   // echo "success";
}
else{
    echo "database not connected";
}

?>