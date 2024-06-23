import mysql.connector
import pandas as pd

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'phonepe_pulse'
}

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pulse_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        metric_name VARCHAR(255),
        metric_value FLOAT,
        timestamp DATETIME,
        latitude FLOAT,
        longitude FLOAT
    )
    """)

def insert_data():
    data = pd.read_csv('transformed_data.csv')
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    create_table(cursor)
    
    for _, row in data.iterrows():
        cursor.execute("""
        INSERT INTO pulse_data (metric_name, metric_value, timestamp, latitude, longitude)
        VALUES (%s, %s, %s, %s, %s)
        """, (row['metric_name'], row['metric_value'], row['timestamp'], row['latitude'], row['longitude']))
    conn.commit()
    cursor.close()
    conn.close()
    print('Data inserted into database')

if __name__ == "__main__":
    insert_data()
