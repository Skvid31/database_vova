import sqlite3


def create_tables():
    with sqlite3.connect('electronics_store.db') as conn:
        cursor = conn.cursor()

        # Create products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')

        # Create customers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')

        # Create orders table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                order_date DATE NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
        ''')

        conn.commit()


def insert_products():
    products = [
        (1, 'iPhone 12', 'смартфони', 799.99),
        (2, 'MacBook Pro', 'ноутбуки', 1299.99),
        (3, 'iPad Pro', 'планшети', 999.99),
        (4, 'Samsung Galaxy S21', 'смартфони', 699.99),
        (5, 'Dell XPS 13', 'ноутбуки', 1099.99)
    ]

    with sqlite3.connect('electronics_store.db') as conn:
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO products (product_id, name, category, price)
            VALUES (?, ?, ?, ?)
        ''', products)
        conn.commit()


def insert_customers():
    customers = [
        (1, 'John', 'Doe', 'john.doe@example.com'),
        (2, 'Jane', 'Smith', 'jane.smith@example.com'),
        (3, 'Alice', 'Johnson', 'alice.johnson@example.com')
    ]

    with sqlite3.connect('electronics_store.db') as conn:
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO customers (customer_id, first_name, last_name, email)
            VALUES (?, ?, ?, ?)
        ''', customers)
        conn.commit()


def insert_orders():
    orders = [
        (1, 1, 1, 2, '2024-07-15'),
        (2, 2, 2, 1, '2024-07-16'),
        (3, 3, 3, 3, '2024-07-17'),
        (4, 1, 4, 1, '2024-07-18'),
        (5, 2, 5, 1, '2024-07-19')
    ]

    with sqlite3.connect('electronics_store.db') as conn:
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date)
            VALUES (?, ?, ?, ?, ?)
        ''', orders)
        conn.commit()


if __name__ == '__main__':
    create_tables()
    insert_products()
    insert_customers()
    insert_orders()
