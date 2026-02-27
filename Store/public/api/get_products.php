<?php 
header('Content-Type: application/json');
require_once __DIR__ . '/db.php';

$stmt = $pdo->query("SELECT id, name, category, price FROM products");
$products = $stmt->fetchAll();
foreach ($products as &$p) {
    $p['price'] = floatval($p['price']);
}
echo json_encode($products);

