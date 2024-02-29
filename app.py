from flask import Flask, request, render_template, url_for,flash,redirect
import datetime
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

        if duser in data_dict and data_dict[duser] == dpass:
            return redirect(url_for('doctor_dashboard'))
        else:
            flash("Invalid Username or Password")

    return render_template('doctor_login.html')

@app.route('/patient-login',methods = ['GET','POST'])
def patient_login(): 
    if request.method == 'POST':
        puser = request.form['username']
        ppass = request.form['password']

        if puser in data_dict and data_dict[puser] == ppass:
            return redirect(url_for('patient_dashboard'))
        else:
            flash("Incorrect Username or Password")
 
    return render_template('patient_login.html')

@app.route('/doctor_dashboard',methods = ['GET','POST'])
def doctor_dashboard():
    return render_template('doctor_form.html')

@app.route('/patient-dashboard')
def patient_dashboard():
    return "Hey there, Patient"


if __name__ == '__main__':
    app.run(debug=True)