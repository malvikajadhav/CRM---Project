import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'shlok'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE CRMco")

print("All Done!")