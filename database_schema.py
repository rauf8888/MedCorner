import sqlite3

db = sqlite3.connect('database.db')
cursor = db.cursor()

stringToExcecute1 = '''CREATE TABLE IF NOT EXISTS DOCTOR_RECORDS(DID int PRIMARY KEY,
                    DName VARCHAR(256), USERNAME TEXT, PASSWORD TEXT) '''
cursor.execute(stringToExcecute1)

stringtoExcecute2 = '''CREATE TABLE IF NOT EXISTS PATIENT_DETAILS(PId int primary key, PNAME TEXT, USERNAME TEXT, PASSWORD TEXT)'''
cursor.execute(stringtoExcecute2)
 
print('OH YEAH MAMA MIAA')

stringToExecute3 = '''SELECT PNAME from PATIENT_DETAILS'''
cursor.execute(stringToExecute3)
result=cursor.fetchall()
print(result)
a = 0
for i in result:
    stringToExecute4 = '''CREATE TABLE IF NOT EXISTS {}(DATE TEXT, ADVICE TEXT, PRESCRIPTION TEXT, AUDIO TEXT)'''.format(i[0])
    cursor.execute(stringToExecute4)
    print("Table Created Successfully ")
    a=+1

db.commit()
cursor.close()