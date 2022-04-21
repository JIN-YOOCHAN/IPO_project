import os
from re import A
from flask import Flask
from routes import user_routes
from flask import render_template
import csv


def create_app():
  app = Flask(__name__)
  app.register_blueprint(user_routes.bp)
  
  return app.run()

if __name__ == "__main__":
  app = create_app()
  app.run()
