import pandas as pd
import mysql.connector

# Load the Excel file
excel_file = 'C:\\xampp2\\htdocs\\Project 1\\MOCK_DATA-_3_.xlsx'  # Update this path
df = pd.read_excel(excel_file)



df = df.where(pd.notnull(df), None)
# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',  # Update with your MySQL username
    password='',  # Update with your MySQL password
    database='project_1'  # Update with your database name
)

cursor = conn.cursor()

# Insert data into the database
for index, row in df.iterrows():
    sql = "INSERT INTO  project_1_table (order_date, product_id, product_name, product_category, customer_name, customer_phone_number, no_of_products_buy,product_purchase_price, product_sale_price,profit_margin, loss_margin, year, region,country, state, city) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)"
    values = (row['order_date'], row['product_id'], row['product_name'], row['product_category'], row['customer_name'],
              row['customer_phone_number'], row['no_of_products_buy'], row['product_purchase_price'],
              row['product_sale_price'], row['profit_margin'],
              row['loss_margin'], row['year'],
              row['region'], row['country'],
              row['state'], row['city'])  # Update column names
    cursor.execute(sql, values)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Data inserted successfully!")
