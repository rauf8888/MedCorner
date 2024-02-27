from flask import Flask, request, render_template, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "ThisIsASecretKey@1234"

@app.route('/')
def landing_page(): 
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)