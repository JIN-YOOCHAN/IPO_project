from flask import Blueprint
from flask import render_template
import psycopg2
import csv


connection = psycopg2.connect(database="project3", user="jinyoochan")
cursor = connection.cursor()
cursor.execute("""
SELECT *
FROM ipo_data;
""")
rows = cursor.fetchall()
print(type(rows))