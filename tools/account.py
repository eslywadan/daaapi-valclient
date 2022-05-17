from dbtools.db_connection import DbConnection
import tools.crypto as crypto
import pandas as pd
from dbtools.sql_buffer import SqlBuffer
from datetime import datetime


def get_client_info(client_id):
    sql = '''
    SELECT CLIENT_ID, PASSWORD, TYPE, EXPIRY, PERMISSION 
      FROM ACCOUNT'''
    buf = SqlBuffer(sql).add("CLIENT_ID", client_id)
    cn = DbConnection.default()
    df = pd.read_sql_query(buf.sql, cn)

    info = df.to_dict()
    
    return info

