from flask import Blueprint
from flask import render_template
from flask import jsonify
import pandas as pd
import psycopg2
import csv
import json

bp = Blueprint("user", __name__, url_prefix='/')

@bp.route('/', methods=["POST", "GET"])
def main():
  table = pd.read_csv("ipo_table.csv")
  header = list(table.columns)
  name = list(table.iloc[:,0])
  predict = list(table.iloc[:,1])
  profit = list(table.iloc[:,2])
  return render_template('main.html',table_header = table, table_name =name, table_predict = predict, table_profit = profit)

@bp.route('/api', methods=["POST", "GET"])
def api():
  connection = psycopg2.connect(database="project3", user="jinyoochan")
  cursor = connection.cursor()
  cursor.execute("""
  SELECT *
  FROM ipo_data;
  """)
  rows = cursor.fetchall()

  headers=["name","market","sectors","price_hoping","price_real",
        "inv_comp","stock_amount","stock_fund","exec_company","listing_date","percent_newstock","percent_invest",
        "percent_personal","percent_lock_up","capital","company_size","profit"]

  rows = headers+rows
  
  return jsonify(rows)
