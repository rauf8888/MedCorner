from flask import Flask, request, render_template, url_for,flash
import sqlite3

app = Flask(__name__)
app.secret_key = "ThisIsASecretKey@1234"

data_dict = {"rauf":"12345","Dharshan":'67890'}

@app.route('/home')
def landing_page(): 
    return render_template('landing.html')

@app.route('/doctor-login',methods = ['GET','POST'])
def doctor_login():
    if request.method == 'POST':
        duser = request.form['username']
        dpass = request.form['password']

        print(duser,dpass)

    return render_template('doctor_login.html')

@app.route('/patient-login',methods = ['GET','POST'])
def patient_login(): 
    if request.method == 'POST':
        puser = request.form['username']
        ppass = request.form['password']

        print(puser,ppass)   
 
    return render_template('patient_login.html')

if __name__ == '__main__':
    app.run(debug=True)