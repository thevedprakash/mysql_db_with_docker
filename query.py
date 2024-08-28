import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='127.0.0.1',          # Use '127.0.0.1' instead of 'localhost'
    port=3308,                 # Ensure the port is correct
    user='root',           
    password='123456',  
    database='superstore_test' 
)

# Create a cursor object
cursor = connection.cursor()

# Write your SQL query
query = "SELECT * FROM sample_store LIMIT 10;"

# Execute the SQL query
cursor.execute(query)

# Fetch all the rows from the result of the query
rows = cursor.fetchall()

# Iterate through the rows and print them
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
