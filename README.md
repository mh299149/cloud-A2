# 🛍️ Product API – Flask + MySQL

A simple RESTful API built using Flask and PyMySQL to store and retrieve product data from a MySQL database.

---

## 🚀 Features

- `POST /store-products` – Store multiple products in the database.
- `GET /list-products` – Fetch all stored products.

---

## 🧠 Tech Stack

- **Backend:** Python (Flask)
- **Database:** MySQL (AWS RDS or local)
- **Driver:** PyMySQL

---

## 📦 API Endpoints

### ➕ `POST /store-products`

Store product data.

#### Request Body:

```json
{
  "products": [
    {
      "name": "Product 1",
      "price": 99.99,
      "availability": true
    },
    {
      "name": "Product 2",
      "price": 49.99,
      "availability": false
    }
  ]
}
````

#### Response (Success - 200):

```json
{
  "message": "Success"
}
```

#### Error Responses:

* `400 Bad Request` – Invalid input format.
* `500 Internal Server Error` – Server or DB issue.

---

### 📄 `GET /list-products`

Retrieve all products.

#### Response (Success - 200):

```json
{
  "products": [
    {
      "id": 1,
      "name": "Product 1",
      "price": 99.99,
      "availability": true
    },
    ...
  ]
}
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask pymysql
```

### 4. Run the Flask App

```bash
python app.py
```

The server will start at: `http://127.0.0.1:5000/`

---

## 🧾 MySQL Table Schema

Before running the app, create this table in your MySQL database:

```sql
CREATE TABLE products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  availability BOOLEAN NOT NULL
);
```

---

## 🔐 Security Warning

⚠️ **Do not hardcode sensitive information like DB credentials.**
Use environment variables or `.env` + `python-dotenv` for production deployments.
