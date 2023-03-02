import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="God@1234",
  database="mydatabase"

)



mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("SHOW DATABASES")

# for i in mycursor:
#     print(i)


# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("SHOW TABLES")

# for i in mycursor:
#     print(i)

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

mycursor.execute("DESCRIBE customers")
for i in mycursor:
    print(i)