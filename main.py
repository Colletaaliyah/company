from flask import Flask,render_template
import psycopg2
app=Flask(__name__)

#Connect to an existing database
conn = psycopg2.connect(user="postgres", password="Candidcoco@20", host="localhost",
                         port="5432", database="Company")
# a connection creates a session.
#a session is the period in which you’re  connected or logged in into your db. 
#Open a cursor to perform database operations
cur = conn.cursor()




@app.route('/')
def hello_world():
    name='aaliyah'
    return render_template('index.html',name=name)

@app.route('/customers')
def customers():
     cur.execute('select * from customers')
     customers=cur.fetchall()
     print(customers)
     return render_template("customers.html",customers=customers)


if __name__=="__main__":
    app.run()