from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Manuel123*@localhost:3306/store_db")

meta = MetaData()

conn = engine.connect()