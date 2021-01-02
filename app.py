import mysql.connector

from flask import Flask, render_template, request
app = Flask(__name__)

mydb = mysql.connector.connect(host="localhost", user="root", passwd="7019252847", database="workshop")
c = mydb.cursor()
c.execute("USE workshop;")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def aboutus():
    return render_template("aboutus.html")

@app.route("/add_orders")
def add_orders():
    return render_template("add_orders.html")

@app.route("/add_orders_button", methods=['POST'])
def add_orders_record():
    Order_id = request.form.get("Order_id")
    Customer_Name = request.form.get("Customer_Name")
    Phone = request.form.get("Phone")

    c.execute("""
                INSERT INTO Orders(Order_id,Customer_Name, Phone) VALUES(%s,%s,%s)
                """, (Order_id,Customer_Name, Phone,))
    mydb.commit()
    return "Successfully added a Order data"

@app.route('/view_orders')
def render_all_orders():
    c.execute("""SELECT * FROM Orders""")
    order_query=c.fetchall()

    return render_template("order_details.html", orders=order_query)

@app.route('/delete_orders_button', methods=['POST'])
def delete_orders():
    Order_id = request.form.get("Order_id")

    c.execute("""
            DELETE FROM Orders WHERE Order_id=%s
            """,(Order_id,))
    mydb.commit()
    return "Order deleted Successfully"