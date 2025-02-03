
<?php
if(isset($_POST['submit'])){
//for table
$name1 = $_POST['column1'];
$name2 = $_POST['column2'];
$name3 = $_POST['column3'];
$name4 = $_POST['column4'];

//FOR ADD MORE TABLES
//$name4 = $_POST['column5'];
//$name4 = $_POST['column5'];
//$name4 = $_POST['column5'];

// for connect to the db
$servername  = "localhost";
$username  = "root";
$password  = "";
$name = $_POST['name'];
     //change
$database = $name;
//create a connection
$conn = mysqli_connect($servername,$username,$password,$database);

  //ADD VARIABLE NAME (CHANGABLE)
 
$sql = "CREATE TABLE $database ( `SN.` INT NOT NULL AUTO_INCREMENT , `$name1` VARCHAR(255) NOT NULL , `$name2` VARCHAR(255) NOT NULL , `$name3` VARCHAR(255) NOT NULL, `$name4` VARCHAR(255) NOT NULL, PRIMARY KEY (`SN.`))";

$result = mysqli_query($conn, $sql);

    // for check the connection
if($result){
    echo "<script> alert ('tables created') </script>";
//echo "done";
echo "<br>";
 }
else{
//echo "the table was not created or created already"."<br>".mysqli_error($conn);
echo "<br>";
}
}
?>

<?php
      $value1 = $name1;
      $value2 = $name2;
      $value3 = $name3;
      $value4 = $name4;
 ?>
      
<?php
// for collect
if(isset($_POST['submit'])){
$name = $_POST['name'];
$servername  = "localhost";
$username  = "root";
$password  = "";
$database = $name;

//create a connection
$conn = mysqli_connect($servername,$username,$password,$database);
if(!$conn){
    die ("sorry database connection was failed" . mysqli_connect_error());
    echo "<br>";
    }
    else{
   // echo "done";
    //echo "<br>";
    }
                    //change
$sql = "SELECT * FROM $database";

$result = mysqli_query($conn, $sql);
//echo "done";
//echo "<br>";
$num = mysqli_num_rows($result);
//echo "data<br>"; 
}
?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>collect</title>
</head>

<body>
    <div class="container">
        <form action="collect.php" method= "post">
        <h3>collected data :</h3>
            <input type="text" name ="name" placeholder="ENTER DB NAme" value="<?php echo $database;?>"?>
            <input type="submit" name= "click"  >
        </form>
        <div class="form">
            <form action="collect.php" method ="post">
          
               
                 <h7>total data:
                    <?php
                    if(isset($_POST['submit'])){
                    echo $num;
                    }
                    ?>
                </h7>
             </form>
             </div>
        <div class="center">
        <table> <?php//change?>
                <tr id ="header">
                    <th>SN.</th>
                    <th><?php echo $value1;?> </th>
                    <th><?php echo $value2;?> </th>
                    <th><?php echo $value3;?> </th>
                    <th><?php echo $value4;?> </th>
                </tr>
                    <?php
                   // if(isset($_POST[''])){
                    if($num > 0){  //change
                        while($row = mysqli_fetch_assoc($result)){
                    echo '<tr>'. '<td>'.$row['SN.'].'.</td>'.
                              '<td>'.$row[$value1].'</td>'. 
                              '<td>'.$row[$value2].'</td>'.
                              '<td>'.$row[$value3].'</td>'.
                              '<td>'.$row[$value4].'</td>'.
                             '</tr>';
                      //  echo var_dump($row);
                        echo "<br>";
                     //   }
                    }
                    }
                    ?>
            </table><br>
        </div>
    </div>
</body>
<style>
    body {
        background-color: #f5f0e1;
        padding: 0;
        margin: 0;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        text-align: center;
    }
    table{
    position: absolute;
    background-color: rgb(252, 255, 249);
    border-collapse: collapse;
    top: 40%;
    left: 28%;
    width: 600px;
    height: 50px;
    border: 1px solid #bdc3c7;
    
}
th,td{
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

#header{
    background-color: #587e76;
    color: #fff;
    padding: 10px;
}

.container form {
        color: rgb(0, 0, 0);
        font-size: 25px;
        padding: 1px;
    }

    #button {
        padding: 5px 15px;
        font-size: 20px;
        background-color: #ff6e40;
        border-radius: 10px;
        border-color: #ff6e40;
        color: white;
        text-decoration: none;
    }
    .form h6{
        color: black;
    }
    .form p{
        font-size: 20px;
    } 
    .container form input{
        padding: 5px 8px;
        font-size: 15px;
        background-color: white;
        border-radius: 10px;
        border-color: #ff6e40;
        color: black;
        text-decoration: none;

    }
</style>
</html>
