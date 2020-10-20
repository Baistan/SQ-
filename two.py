import sqlite3
import pprint
connection = sqlite3.connect('test.db')

cursor = connection.cursor()

# sql_command = """CREATE TABLE salary(
# staff_id INTEGER PRIMARY KEY,
# full_name VARCHAR(50),
# staff_salary INTEGER(20),
# join_date DATE);"""

# cursor.execute("INSERT INTO salary VALUES(1,'Baistan',30000,'2020-01-10')")
# cursor.execute("INSERT INTO salary VALUES(2,'Baistan',35000,'2020-02-10')")
# cursor.execute("INSERT INTO salary VALUES(3,'Baistan',40000,'2020-03-10')")
# cursor.execute("INSERT INTO salary VALUES(4,'Baistan',45000,'2020-04-10')")
# cursor.execute("INSERT INTO salary VALUES(5,'Baistan',50000,'2020-05-10')")
# cursor.execute("INSERT INTO salary VALUES(6,'Baistan',55000,'2020-06-10')")
# cursor.execute("INSERT INTO salary VALUES(7,'Baistan',60000,'2020-07-10')")
# cursor.execute("INSERT INTO salary VALUES(8,'Baistan',65000,'2020-08-10')")
# cursor.execute("INSERT INTO salary VALUES(9,'Baistan',70000,'2020-09-10')")
# cursor.execute("INSERT INTO salary VALUES(10,'Baistan',75000,'2020-10-10')")
# cursor.execute("INSERT INTO salary VALUES(11,'Baistan',80000,'2020-11-10')")
# cursor.execute("INSERT INTO salary VALUES(13,'Baistan',85000,'2020-12-10')")
# cursor.execute("INSERT INTO salary VALUES(14,'Baistan',90000,'2021-01-10')")
# cursor.execute("INSERT INTO salary VALUES(15,'Baistan',95000,'2020-02-10')")
# cursor.execute("INSERT INTO salary VALUES(16,'Baistan',100000,'2020-03-10')")

cursor.execute("SELECT * FROM salary WHERE full_name IN ('Alina','Erjan','Maksim') AND staff_salary >20000;")

ans = cursor.fetchall()

pprint.pprint(ans)

connection.commit()
connection.close()