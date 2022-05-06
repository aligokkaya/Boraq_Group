
from sqlalchemy import create_engine,MetaData
meta = MetaData()
def con():
    conn = create_engine("mysql+pymysql://hypegena:aZ5xjXf133@hypegenai.com/hypegena_b_challenge",
                        echo=False,
                        connect_args={'connect_timeout': 300})
    
    connect = conn.connect()
    return connect

