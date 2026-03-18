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

    case 'create';
        $name = $_POST['name'];
        $category = $_POST['category'];
        $price = $_POST['price'];
        $stmt = $pdo->prepare(
            "INSERT INTO products (name, category, price) VALUES (?,?,?)" 
            );
            $stmt->execute([$name, $category, $price]);
            echo json_encode(["success" => true]);
        break;
    
    case 'update';
        $id = $_POST['id'];
        $name = $_POST['name'];
        $category = $_POST['category'];
        $price = $_POST['price'];
        $stmt = $pdo->prepare(
            "UPDATE products SET name=?, category=?, price=? WHERE id=?"
        );
        $stmt->execute([$name, $category, $price]);
        echo json_encode(["success" => true]);
        break;
    
    case 'delete';
    $id - $_POST['id'];
    $stmt = $pdo->prepare("DELETE FROM products WHERE id=?");
    $stmt->execute([$id]);
    echo json_encode(["success" => true]);
         break;

    case 'read';

    $stmt = $pdo->query(
        "SELECT id, name, category, price FROM products"
    );
    echo json_encode($stmt->fetchAll());
    break;
    };
    };
  

