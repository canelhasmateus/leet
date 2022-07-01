from sqlalchemy import create_engine

HOST = "qads.chila6xoexmk.us-east-1.rds.amazonaws.com"
USER = "admin"
PORT = 3306
PASSWORD = "Qads!2021"
DATABASE = "qads"
engine = create_engine( f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}" )
