import sqlite3

def get_total_sales():
    with sqlite3.connect('electronics_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT SUM(p.price * o.quantity) AS total_sales
            FROM orders o
            JOIN products p ON o.product_id = p.product_id
        ''')
        total_sales = cursor.fetchone()[0]
        return total_sales

def get_order_count_per_customer():
    with sqlite3.connect('electronics_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT c.first_name, c.last_name, COUNT(o.order_id) AS order_count
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            GROUP BY c.customer_id
        ''')
        return cursor.fetchall()

def get_average_order_value():
    with sqlite3.connect('electronics_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT AVG(p.price * o.quantity) AS average_order_value
            FROM orders o
            JOIN products p ON o.product_id = p.product_id
        ''')
        average_order_value = cursor.fetchone()[0]
        return average_order_value

def get_most_popular_category():
    with sqlite3.connect('electronics_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT p.category, COUNT(o.order_id) AS order_count
            FROM orders o
            JOIN products p ON o.product_id = p.product_id
            GROUP BY p.category
            ORDER BY order_count DESC
            LIMIT 1
        ''')
        most_popular_category = cursor.fetchone()[0]
        return most_popular_category

def get_product_count_per_category():
    with sqlite3.connect('electronics_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT category, COUNT(*) AS product_count
            FROM products
            GROUP BY category
        ''')
        return cursor.fetchall()

def update_smartphone_prices():
    with sqlite3.connect('electronics_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE products
            SET price = price * 1.10
            WHERE category = 'смартфони'
        ''')
        conn.commit()
