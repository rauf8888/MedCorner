from flask import Flask, request, render_template, url_for,flash,redirect,session
from datetime import date
import sqlite3
from werkzeug.security import check_password_hash


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
    query = "SELECT * FROM DOCTOR_RECORDS"
    cursor.execute(query)
    result = cursor.fetchall() 
    if request.method == 'POST':
        duser = request.form['username']
        dpass = request.form['password']
        session['username'] = duser
        x = False

        for users in result:
            if duser in users[2] or check_password_hash(users[3],dpass):
                x = True
                return redirect(url_for('doctor_dashboard'))
        if x == False:
            flash("Invalid Username or Password")

    return render_template('doctor_login.html')

@app.route('/patient-login',methods = ['GET','POST'])
def patient_login(): 
    query = "SELECT * FROM PATIENT_DETAILS"
    cursor.execute(query)
    result = cursor.fetchall() 
    if request.method == 'POST':
        puser = request.form['username']
        ppass = request.form['password']
        session['username'] = puser
        x = False

        for users in result:
            if puser in users[2] or check_password_hash(users[3],ppass):
                x = True
                return redirect(url_for('patient_dashboard'))
        if x == False:
            flash("Invalid Username or Password")
 
    return render_template('patient_login.html')

@app.route('/doctor_dashboard',methods = ['GET','POST'])
def doctor_dashboard():

    duser = session.get('username')
    query = 'SELECT DName FROM DOCTOR_RECORDS WHERE USERNAME = ?'
    cursor.execute(query,(duser,))
    record = cursor.fetchone()
    dname = record[0].capitalize()

    if request.method == 'POST':
        try:
            date_today = date.today().strftime('%Y-%m-%d')
            patient_name = request.form['dropdown']
            advice = request.form['textfield1']
            prescription = request.form['textfield2']
            audio_file = request.files['audio']
            ext =audio_file.filename.split('.')
            new_filename = f"{patient_name}{date_today}.{ext[1]}"
            audio_file.filename = new_filename
            save_path = 'Advisory_Audios/'+new_filename
            audio_file.save(save_path)

            command = """INSERT INTO {} VALUES(?,?,?,?)""".format(patient_name)
            cursor.execute(command, (date_today,advice,prescription,new_filename))
            connection.commit()
            flash("Data Inserted Successfully!")
        except:
            flash("Error While Writing into Database")
    return render_template('doctor_form.html',dname=dname)

@app.route('/patient-dashboard')
def patient_dashboard():
    return "Hey there, Patient"


if __name__ == '__main__':
    app.run(debug=True)