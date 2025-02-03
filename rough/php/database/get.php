<?php

//for access the session data
session_start();

if(isset($_SESSION['pass'])){
echo "your username is ".$_SESSION['username']."<br>"."password is ". $_SESSION['pass'];

echo "<br>";
echo "session completed";
}

else
    echo "<br>please check your username ";

?>