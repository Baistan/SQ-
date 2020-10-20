import sqlite3

connection =  sqlite3.connect('test.db')


cursor = connection.cursor()


# sql_command = """CREATE TABLE products(
# product_id  INTEGER PRIMARY KEY,
# product_name varchar(20),
# product_description varchar(50),
# customer varchar (20),
# pub_date DATE);"""


# sql_command = """INSERT INTO products VALUES(4,"OPPO G6","The China SMARTPhone","Danil","2020-10-19");"""
# cursor.execute(sql_command)

cursor.execute("SELECT * FROM products WHERE product_name='Apple Watch'")

ans = cursor.fetchall()
print(ans)



connection.commit()
connection.close()