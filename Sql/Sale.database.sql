-- =============================================
-- Sales Inventory Management System
-- Database: Sales
-- Table: products
-- =============================================

-- Create Database
CREATE DATABASE Sales;
GO

-- Select Database
USE Sales;
GO

-- Create Products Table
CREATE TABLE products
(
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10,2),
    Quantity INT,
    OrderDate DATE
);
GO

-- Insert Sample Data
INSERT INTO products
(
    ProductID,
    ProductName,
    Category,
    Price,
    Quantity,
    OrderDate
)
VALUES
(1, 'Laptop', 'Electronics', 55000.00, 10, '2026-01-05'),
(2, 'Wireless Mouse', 'Electronics', 1200.00, 25, '2026-01-07'),
(3, 'Keyboard', 'Electronics', 1800.00, 20, '2026-01-10'),
(4, 'Office Chair', 'Furniture', 7500.00, 15, '2026-01-12'),
(5, 'Study Table', 'Furniture', 9500.00, 8, '2026-01-15'),
(6, 'T-Shirt', 'Clothing', 799.00, 40, '2026-01-18'),
(7, 'Jeans', 'Clothing', 1599.00, 30, '2026-01-20'),
(8, 'Running Shoes', 'Sports', 2999.00, 18, '2026-01-22'),
(9, 'Football', 'Sports', 999.00, 25, '2026-01-25'),
(10, 'Cricket Bat', 'Sports', 2499.00, 12, '2026-01-28'),
(11, 'Rice 5kg', 'Grocery', 450.00, 50, '2026-02-01'),
(12, 'Cooking Oil 1L', 'Grocery', 150.00, 60, '2026-02-03'),
(13, 'Notebook', 'Books', 120.00, 100, '2026-02-05'),
(14, 'Programming Book', 'Books', 899.00, 20, '2026-02-08'),
(15, 'Water Bottle', 'Other', 499.00, 35, '2026-02-10'),
(16, 'Headphones', 'Electronics', 2200.00, 22, '2026-02-12'),
(17, 'Monitor', 'Electronics', 14500.00, 7, '2026-02-15'),
(18, 'Bookshelf', 'Furniture', 6500.00, 10, '2026-02-18'),
(19, 'Jacket', 'Clothing', 2499.00, 14, '2026-02-20'),
(20, 'Backpack', 'Other', 1299.00, 28, '2026-02-22');
GO

-- View Products
SELECT *
FROM products;
GO