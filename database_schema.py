import sqlite3

db = sqlite3.connect('database.db')
cursor = db.cursor()

stringToExcecute1 = '''CREATE TABLE IF NOT EXISTS DOCTOR_RECORDS(DID int PRIMARY KEY,
                    DName VARCHAR(256), USERNAME TEXT, PASSWORD TEXT) '''
cursor.execute(stringToExcecute1)

stringtoExcecute2 = '''CREATE TABLE IF NOT EXISTS PATIENT_DETAILS(PId int primary key, PNAME TEXT, USERNAME TEXT, PASSWORD TEXT)'''
cursor.execute(stringtoExcecute2)
 
print('OH YEAH MAMA MIAA')

db.commit()
cursor.close()