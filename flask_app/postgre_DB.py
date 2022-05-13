import psycopg2
import pandas as pd

def total_to_db():
  connection = psycopg2.connect(database="project3", user="jinyoochan")
  cursor = connection.cursor()

  df = pd.read_csv("/Users/jinyoochan/Desktop/project/flask_app/Data/total_to_db.csv")

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS ipo_data(
    name VARCHAR(255) PRIMARY KEY,
    market VARCHAR(255),
    sectors VARCHAR(255),
    price_hoping VARCHAR(255),
    price_real VARCHAR(255),
    inv_comp VARCHAR(255),
    stock_amount VARCHAR(255),
    stock_fund VARCHAR(255),
    exec_company VARCHAR(255),
    listing_date VARCHAR(255),
    percent_newstock VARCHAR(255),
    percent_invest VARCHAR(255),
    percent_personal VARCHAR(255),
    percent_lock_up VARCHAR(255),
    capital VARCHAR(255),
    company_size VARCHAR(255),
    profit VARCHAR(255)
  );
  """)

  cursor.execute("SELECT * FROM ipo_data;")
  result = cursor.fetchall()
  if result==[]:
      
    for i in range(len(df)-1,0-1,-1):
      cursor.execute("""
      INSERT INTO ipo_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
      """, 
      [df.iloc[i,j] for j in range(1,18)])

  else:
    pass

  connection.commit()




def new_to_db():

  connection = psycopg2.connect(database="project3", user="jinyoochan")
  cursor = connection.cursor()

  df = pd.read_csv("/Users/jinyoochan/Desktop/IPO_project/flask_app/Data/new_to_db.csv")
 
  for i in range(len(df)):
    try:
      cursor.execute("""
      INSERT INTO ipo_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
      """, 
      [df.iloc[i,j] for j in range(1,18)])
      connection.commit()

    except Exception as ex:
      print(f"{i},중복값은 추가 X",ex)

