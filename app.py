from flask import *
from flask import Flask, jsonify, request, render_template
import json
import mysql.connector
import stepper as sp

app = Flask(__name__)

# stp = motor()

# Database connection
mydb = mysql.connector.connect( host="localhost", user="root", password="", database="medicine_dispenser")
mycursor = mydb.cursor()

@app.route('/')
def home():
    return render_template('cart.html')


@app.route('/stepper')
def stepper():
    print("hello")
    return render_template("stepper.html")

@app.route('/cart', methods=['POST'])
def cart():
    # POST request
    if request.method == 'POST':
        # retrieveing med id, quantity & total amount from cart.js
        data = json.loads(request.json['ans'])
        totalAmount = request.json['totalAmount']

        # print("data:" + data) # printing dictionary which consist of med id and qty
        # print("totalAmount:" + totalAmount) # printing total amound
        print("\n\n")

        # call rfidReader.readUserId()

        for i in range (len(data)):
            # retrieving dict keys and values into different variables
            med_id = list(data.keys())[i]
            qty = list(data.values())[i]
        
            print(med_id)
            print(qty)

            # inserting data into database
            sql = "INSERT INTO billing (user_id, med_id, bill_quantity, total_expense) VALUES (%s, %s, %s, %s)"
            val = (1, med_id, qty, totalAmount)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        # call stepper motor code
        sp.motor()
        return 'Nothing'



if __name__ == '__main__':
    # put your current IPv4 address in 'host' attribute
    app.run(debug=True, host= '192.168.158.1')
    app.run(debug=True)