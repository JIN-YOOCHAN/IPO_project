import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import flask_app.crawling as crawling
import flask_app.postgre_DB as postgre_DB
from re import A
from flask import Flask
from routes import user_routes
from flask import render_template
import csv



crawling.crawling_total()
postgre_DB.total_to_db()
import flask_app.modeling as modeling


def create_app():
  app = Flask(__name__)
  app.register_blueprint(user_routes.bp)
  return app.run()

# 웹서비스
if __name__ == "__main__":
  app = create_app()
  app.run()
