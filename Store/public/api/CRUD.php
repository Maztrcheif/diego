<?php
header('Content-type: application/json');
require_once __DIR__ . '/db.php';

if (isset($_POST['action'])) {
    $action = $_POST['action'];
} elseif (isset($_GET['action'])){
    $action = $_GET['action'];
}



try {
    switch ($action) {

    case 'create'
        $name = $_POST['name']
        $category = $_POST['category']
        $price = $_POST['price']
        $stmt = $_POST->prepare(
            "INSERT INTO products (name, category, price") VALUES (?,?,?)"
            );
    break;
    }
    }


