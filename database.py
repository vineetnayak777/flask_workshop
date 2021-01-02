import mysql.connector

def init_db():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="7019252847", database="workshop")
    c = mydb.cursor()
    c.execute("USE workshop;")

    c.execute("""
                CREATE TABLE Orders(
                    Order_id int primary key,
                    Customer_Name varchar(15),
                    Phone bigint
                );
                """)
    mydb.commit()

init_db()