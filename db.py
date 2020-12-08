import mysql.connector
import hashlib
import random

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="db"
)

cursor = db.cursor(buffered=True)

def register(user,passw,cwpassw):
    username = user
    password = passw
    confirmPassword = cwpassw
    
    cursor.execute("SELECT username FROM users WHERE username = %s", (username,))            
    exists = cursor.fetchone()

    if username == "" or password == "" or confirmPassword == "":
         outputMsg = "Enter both a username and a password"
    elif len(password) < 8:
        outputMsg = "Your chosen password is too short(min.8)"
    elif password != confirmPassword:
        outputMsg = "Make sure passwords match"
    elif exists != None:
        outputMsg = "Username already taken"
    else:
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        salt = []
        for i in range(16):
            salt.append(random.choice(alphabet))
        salt = "".join(salt)
        hashed_pass = hashlib.sha256(password.encode("utf-8") + salt.encode("utf-8"))
        password = hashed_pass.hexdigest()
        data = (username, password, salt)
        cursor.execute("INSERT INTO users (username, password, salt) VALUES (%s,%s,%s)", data)
        db.commit()
        outputMsg = "Account successfully made"
    return outputMsg

def login(user, passw):
    username = user
    password = passw
    
    cursor.execute("SELECT username FROM users WHERE username = %s", (username,))            
    exists = cursor.fetchone()
    
    if username == "" or password == "":
        outputMsg = "Enter both a username and a password"
    elif exists == None:
        outputMsg = "Try again"
    else:
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))            
        realPassword = cursor.fetchone()
        strPassword = "".join(realPassword)
        cursor.execute("SELECT salt FROM users WHERE username = %s", (username,))
        salt = cursor.fetchone()
        strSalt = "".join(salt)
        hashed_pass = hashlib.sha256(password.encode("utf-8") + strSalt.encode("utf-8")).hexdigest()
        if hashed_pass == strPassword:
            outputMsg = "Logged in"
        else:
            outputMsg = "Try again"
    return outputMsg

