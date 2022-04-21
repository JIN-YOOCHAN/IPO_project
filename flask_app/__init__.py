import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import flask_app.crawling as crawling
import flask_app.postgre_DB as postgre_DB
import flask_app.modeling as modeling
from re import A
from flask import Flask
from routes import user_routes
from flask import render_template
import csv


def create_app():
  app = Flask(__name__)
  app.register_blueprint(user_routes.bp)
  
  return app.run()


crawling.crawling_new()
postgre_DB.new_to_db()


if __name__ == "__main__":
  app = create_app()
  app.run()
