<?php

//for end/destroy the session

session_start();
session_unset();
session_destroy();

echo "session stopped";

?>