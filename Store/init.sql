CREATE TABLE IF NOT EXISTS products (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	category VARCHAR(255),
	price DECIMAL(6,2) NOT NULL
);

INSERT INTO products (name, category, price) VALUES
('Banana', 'produce', 1.99),
('Apple', 'produce', 1.49),
('Concha', 'bakery', .99),
('Donut', 'bakery', .99),
('Beef', 'meat', 5.99),
('Chicken', 'meat', 4.99),
('Rice', 'grocery', 2.99);
