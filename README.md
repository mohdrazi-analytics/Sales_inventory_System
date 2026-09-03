# 📦 Sales Inventory Management System

A **Sales & Inventory Management System** built using **Python, Streamlit, and Microsoft SQL Server**.

This project provides a simple web-based interface to manage products and inventory data with SQL Server as the backend database.

## 🚀 Features

* 📊 Interactive Dashboard
* ➕ Add New Products
* 👀 View Products
* ✏️ Update Product Information
* 🗑️ Delete Products
* 🗄️ SQL Server Database Integration
* 🐍 Python-based application
* 🌐 Streamlit Web Interface

## 🛠️ Technologies Used

| Technology     | Purpose                 |
| -------------- | ----------------------- |
| 🐍 Python      | Application development |
| 🎈 Streamlit   | Web application & UI    |
| 🗄️ SQL Server | Database                |
| 🔌 PyODBC      | SQL Server connection   |
| 📊 Pandas      | Data handling           |

## 🏗️ Project Architecture

```text
User
  ↓
Streamlit Application
  ↓
Python
  ↓
PyODBC
  ↓
Microsoft SQL Server
  ↓
Sales & Inventory Data
```

## 📂 Project Structure

```text
Sales_inventory_System/
│
├── app.py
├── sales.py
├── machine.ipynb
├── db_connection.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/mohdrazi-analytics/Sales_inventory_System.git
```

### 2. Open the project

```bash
cd Sales_inventory_System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

## 🗄️ Database

This project uses **Microsoft SQL Server** to store and manage inventory information.

The application connects to SQL Server using **PyODBC**.

> Database credentials should be stored securely and should never be uploaded to GitHub.

## 📸 Screenshots

Screenshots of the application can be added here to demonstrate the dashboard and inventory management features.

## 🎯 Project Goal

The goal of this project is to demonstrate practical experience in:

* Database management
* SQL Server
* Python
* Streamlit application development
* CRUD operations
* Database connectivity
* Inventory management

## 👨‍💻 Author

**Mohd Razi**

📊 Data Analyst → Data Engineer

---

⭐ If you find this project useful, consider giving it a star!
