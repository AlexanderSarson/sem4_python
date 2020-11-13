import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data/people.csv')
con_str = "mysql+mysqlconnector://root:root@db/db"
engine = create_engine(con_str)
df = df.applymap(str)
df.to_sql('people',con=engine, if_exists='append', index = False)