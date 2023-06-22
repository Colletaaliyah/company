from flask import Flask,render_template,request,redirect
from mytestpostgres import fetch_data
from mytestpostgres import insert_customers



app=Flask(__name__)

#Connect to an existing database

# a connection creates a session.
#a session is the period in which you’re  connected or logged in into your db. 
#Open a cursor to perform database operations






@app.route('/')
def hello_world():
    name='aaliyah'
    return render_template('index.html',name=name)

# @app.route('/customers')
# def customers():
#      cur.execute('select * from customers')
#      customers=cur.fetchall()
#      print(customers)
#      return render_template("customers.html",customers=customers)


@app.route('/customers')
def customers():
    customers=fetch_data('customers')
    return render_template("customers.html",customers=customers)



@app.route("/addcustomers",methods=['POST','GET'])
def addcustomers():
    if request.method=='POST':
        first_name=request.form["first_name"]
        last_name=request.form["last_name"]
        email=request.form['email']
        phone=request.form["phone"]
        print(first_name)
        print(last_name)
        print(email)
        print(phone)
        customer=(first_name,last_name,email,phone)
        insert_customers(customer)
        return redirect("/customers")



# if __name__=="__main__":
app.run(debug=True)