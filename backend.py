# backend_fin.py
import psycopg2
import pandas as pd
from datetime import date

# Database configuration
DB_NAME = "adhar system america"
DB_USER = "postgres"
DB_PASSWORD = "Sakshi@299"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_connection():
    """Establishes and returns a new database connection."""
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def setup_database():
    """Creates the transactions table if it doesn't exist."""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id VARCHAR(255) PRIMARY KEY,
                transaction_date DATE NOT NULL,
                description TEXT,
                amount DECIMAL(10, 2) NOT NULL,
                type VARCHAR(20) -- 'Revenue' or 'Expense'
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        return "Database setup successful!"
    except Exception as e:
        return f"Database setup failed: {e}"

# --- CRUD Operations ---

def add_transaction(transaction_id, transaction_date, description, amount, transaction_type):
    """Adds a new transaction to the database."""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO transactions (transaction_id, transaction_date, description, amount, type)
            VALUES (%s, %s, %s, %s, %s);
        """, (transaction_id, transaction_date, description, amount, transaction_type))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Error adding transaction: {e}")
        return False

def get_transactions(transaction_type=None, sort_column='transaction_date', sort_order='DESC'):
    """
    Retrieves all transactions with optional filtering and sorting.
    
    Args:
        transaction_type (str): 'Revenue', 'Expense', or None for all.
        sort_column (str): Column to sort by.
        sort_order (str): 'ASC' or 'DESC'.
    """
    try:
        conn = get_connection()
        query = "SELECT * FROM transactions"
        params = []
        
        if transaction_type:
            query += " WHERE type = %s"
            params.append(transaction_type)

        if sort_column in ['transaction_date', 'amount']:
            query += f" ORDER BY {sort_column} {sort_order}"

        df = pd.read_sql(query, conn, params=params)
        conn.close()
        return df
    except Exception as e:
        print(f"Error getting transactions: {e}")
        return pd.DataFrame()

def update_transaction(transaction_id, transaction_date, description, amount, transaction_type):
    """Updates an existing transaction."""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE transactions
            SET transaction_date = %s, description = %s, amount = %s, type = %s
            WHERE transaction_id = %s;
        """, (transaction_date, description, amount, transaction_type, transaction_id))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Error updating transaction: {e}")
        return False

def delete_transaction(transaction_id):
    """Deletes a transaction by its ID."""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM transactions WHERE transaction_id = %s;", (transaction_id,))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Error deleting transaction: {e}")
        return False

# --- Aggregation and Insights ---

def get_transaction_counts():
    """Returns the total number of all transactions."""
    try:
        conn = get_connection()
        df = pd.read_sql("SELECT COUNT(*) FROM transactions", conn)
        conn.close()
        return int(df.iloc[0, 0])
    except Exception as e:
        print(f"Error getting transaction count: {e}")
        return 0

def get_revenue_sum():
    """Returns the total amount of all revenue transactions."""
    try:
        conn = get_connection()
        df = pd.read_sql("SELECT SUM(amount) FROM transactions WHERE type = 'Revenue'", conn)
        conn.close()
        return float(df.iloc[0, 0]) if df.iloc[0, 0] else 0.0
    except Exception as e:
        print(f"Error getting revenue sum: {e}")
        return 0.0

def get_expense_sum():
    """Returns the total amount of all expense transactions."""
    try:
        conn = get_connection()
        df = pd.read_sql("SELECT SUM(amount) FROM transactions WHERE type = 'Expense'", conn)
        conn.close()
        return float(df.iloc[0, 0]) if df.iloc[0, 0] else 0.0
    except Exception as e:
        print(f"Error getting expense sum: {e}")
        return 0.0