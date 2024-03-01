from flask import Flask, request, render_template, url_for,flash,redirect
from datetime import date
import sqlite3

app = Flask(__name__)
app.secret_key = "ThisIsASecretKey@1234"
data_dict = {"rauf":"12345","Dharshan":'67890'}
connection = sqlite3.connect('database.db',check_same_thread=False)
cursor = connection.cursor()

@app.route('/home')
def landing_page(): 
    return render_template('landing.html')

@app.route('/doctor-login',methods = ['GET','POST'])
def doctor_login():
    query = "SELECT USERNAME,PASSWORD FROM DOCTOR_RECORDS"
    cursor.execute(query)
    result = cursor.fetchall() 
    # print(result)
    if request.method == 'POST':
        duser = request.form['username']
        dpass = request.form['password']

        for users in result:
            if duser in users[0]:
                print("OHH MAMA MIAA")


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
    if request.method == 'POST':
        date_today = date.today().strftime('%Y-%m-%d')
        patient_name = request.form['dropdown']
        advice = request.form['textfield1']
        prescription = request.form['textfield2']
        audio_file = request.files['audio']

        
        print(date_today, patient_name, advice, prescription, audio_file.filename)

    return render_template('doctor_form.html')

@app.route('/patient-dashboard')
def patient_dashboard():
    return "Hey there, Patient"


if __name__ == '__main__':
    app.run(debug=True)