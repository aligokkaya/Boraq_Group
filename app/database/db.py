import mysql.connector

def db_con():
    mydb = mysql.connector.connect(
    host="hypegenai.com",
    user="hypegena",
    password="aZ5xjXf133",
    database="hypegena_b_challenge")
    return mydb
