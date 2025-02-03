<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    
    <title>Registration</title>
</head>
<body>
   
    
    <div class="container">  
        <div class="title">Registration for books</div>
        <form action="connection.php" method="POST" >
             <div class="user-details">                        
                         <div class="input-box">
                             <span class="details">Username </span>
                             <input type="text" name="name" placeholder="Enter Your Username" required >
                         </div>
                         <div class="input-box">
                            <span class="details">Phone no.</span>
                            <input type="number" name="mobile" placeholder="Enter Your Phone Number" required >
                        </div> 
                         <div class="input-box">
                             <span class="details">E-mail </span>
                             <input type="email" name="Email" placeholder="Enter Your Email" required >
                         </div>
                         <div class="input-box">
                             <span class="details">password </span>
                             <input type="password" name="passwords" placeholder="Enter Your password"  required >
                         </div>                            
             </div>
             <div class="button">
                <input type="submit" name="submit" value="Registration">
            </div>
        </form>
    </div>
   
</body>
</html>  


<?php

include 'connection.php';


?>