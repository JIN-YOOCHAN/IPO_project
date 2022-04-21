import psycopg2
import pandas as pd
import numpy

connection = psycopg2.connect(database="project3", user="jinyoochan")
cursor = connection.cursor()

df = pd.read_csv("to_postgre.csv")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ipo_data_clean(
  name VARCHAR(255) PRIMARY KEY,
  market VARCHAR(255),
  sectors VARCHAR(255),
  price_hoping NUMERIC,
  price_real NUMERIC,
  inv_comp NUMERIC,
  stock_amount NUMERIC,
  stock_fund NUMERIC,
  exec_company VARCHAR(255),
  percent_newstock NUMERIC,
  percent_lock_up NUMERIC,
  capital VARCHAR(255),
  company_size VARCHAR(255),
  profit NUMERIC,
  name_spac NUMERIC,
  price_diff NUMERIC,
  inv_comp_cat NUMERIC,
  exec_major NUMERIC,
  exec_quantity NUMERIC,
  listing_year NUMERIC,
  listing_month NUMERIC
);
""")

cursor.execute("SELECT * FROM ipo_data_clean;")
result = cursor.fetchall()
if result==[]:
    
  for i in range(len(df)):
    cursor.execute("""
    INSERT INTO ipo_data_clean VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s);
    """, 
    [df.iloc[i,j] for j in range(0,21)])

else:
  pass


connection.commit()
