import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import flask_app.crawling as crawling
import flask_app.postgre_DB as postgre_DB
from re import A
from flask import Flask
import user_route as user_routes
from flask import render_template
import csv


# 구동(프로그램 새로이 구동시 최초 1번만)
'''
crawling.crawling_total()
postgre_DB.total_to_db()
import flask_app.modeling as modeling


def create_app():
  app = Flask(__name__)
  app.register_blueprint(user_routes.bp)
  return app.run()


if __name__ == "__main__":
  app = create_app()
  app.run()
'''