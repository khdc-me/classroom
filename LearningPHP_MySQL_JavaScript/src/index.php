<?php

$mysqli = new mysqli('mysql', getenv('MYSQL_USER'), getenv('MYSQL_PASSWORD'), 'INFORMATION_SCHEMA');

if ($mysqli->connect_error){
	echo 'Connection error: [', $mysqli->connect_errno, ']: ', $mysqli->connect_error;
} else {
	echo "Connected Successfully to MYSQL container";
}
?>