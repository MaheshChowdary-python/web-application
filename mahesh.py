from  flask import Flask
from flask import render_template , request
import sqlite3 as sql
from sqlite3 import Error

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == "POST":
        try:
            FirstName = request.form['First Name']
            LastName = request.form['Last Name']
            InvoiceNumber = request.form['consignment Number']
            Invoicedate = request.form['consignment date']
            product_name = request.form['Product name']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO customer_comp(first name, last name,invoice,date, product)VALUES(?,?,?,?,?)",
                        (FirstName,LastName,InvoiceNumber,Invoicedate,product_name))

                con.commit()
                Ref_Number = cur.lastrowid
                msg = " Complaint successfully registered please note your reference number:", format(Ref_Number)

        except Error :
            con.rollback()
            msg = "error in registering complaint"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/check')
def check():
   return render_template('update.html')

def update():
    if request.method == 'POST':
        try:
         Ref_Number = request.form('Reference Number')
         with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM customer_comp WHERE ID = Ref_Number')
                rows = cur.fetchall();
        finally:
         return render_template("list.html", rows=rows)








if __name__ == "__main__":
    app.run(debug=True)
