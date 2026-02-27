<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
    rel="stylesheet"/>
    <link rel="stylesheet" href="css/style.css" />
    <title>Valey Harvest</title>
</head>
<body>
    <header>
            <nav class="nav">
                <a href="index.php">Home</a>
                <a href="shop.php">Shop</a>
                <a href="cart.html">Cart</a>
                <a href="apply.html">Apply</a>
                <a href="login.php">Login</a>
            </nav>
    </header>
    <main>
        <div class="login"><form action="login.php" method="post">
            <div><input type="text" placeholder="Username" id="username" name="username"></div>
            <div><input type="password" placeholder="Password" id="password" name="password"></div>
            <div><button type="submit" id="login">Login</button>
                 <button id="create" class="CA">Create Account</button></div>
    </form></div>
    </main>
    <script src="js/login.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>