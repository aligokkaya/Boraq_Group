import mysql.connector
from sqlalchemy import create_engine,MetaData
meta = MetaData()
def db_con():
    mydb = mysql.connector.connect(
    host="hypegenai.com",
    user="hypegena",
    password="aZ5xjXf133",
    database="hypegena_b_challenge")
    return mydb

conn = create_engine("mysql+pymysql://hypegena:aZ5xjXf133@hypegenai.com/hypegena_b_challenge",
                    echo=False,
                    connect_args={'connect_timeout': 600},
                    pool_pre_ping=True)
meta = MetaData(bind=conn)
connect = conn.connect()

