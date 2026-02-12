<?php

$host = "db";
$user = "grocery_user";
$password = "secret";
$database = "grocery";

$conn = new mysqli($host, $user, $password, $database);

if ($conn->connect_error) {
    die("Database connection failed: " . $conn->connect_error);
}
