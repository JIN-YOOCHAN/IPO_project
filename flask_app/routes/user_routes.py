from flask import Blueprint
from flask import render_template
from flask import jsonify
import psycopg2
import csv
import json

bp = Blueprint("user", __name__, url_prefix='/')

@bp.route('/', methods=["POST", "GET"])
def main():
  return render_template('main.html')

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
