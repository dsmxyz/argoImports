import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Hj%mACC#*bFhq&FB47WH6QeT#S2t5oacPYEy3m'

)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE Argo_imports")

print("Database successfully created.")