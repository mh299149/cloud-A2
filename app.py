from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Database connection
def get_db_connection():
    connection = pymysql.connect(
        host='database-as2-final.c8kytdi3nbew.us-east-1.rds.amazonaws.com',  # Use 'localhost' initially for local testing
        user='admin',
        password='5145736735',
        database='mydatabase'
    )
    return connection

@app.route('/store-products', methods=['POST'])
def store_products():
    data = request.json
    if 'products' not in data:
        return jsonify({"message": "Invalid input"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        for product in data['products']:
            sql = "INSERT INTO products (name, price, availability) VALUES (%s, %s, %s)"
            cursor.execute(sql, (product['name'], product['price'], product['availability']))
        conn.commit()
        return jsonify({"message": "Success"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/list-products', methods=['GET'])
def list_products():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        return jsonify({"products": products}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
