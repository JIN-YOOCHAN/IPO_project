import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import flask_app.crawling as crawling
import flask_app.postgre_DB as postgre_DB
from re import A
from flask import Flask
import user_routes
from flask import render_template
from apscheduler.schedulers.background import BackgroundScheduler
import csv

# 웹서비스
if __name__ == "__main__":
  app = create_app()
  app.run()

def create_app():
  app = Flask(__name__)
  app.register_blueprint(user_routes.bp)
  return app.run()

def modeling():
  import flask_app.modeling as modeling
  return modeling


# 매일 변경사항 업데이트
scheduler = BackgroundScheduler({'apscheduler.timezone':'UTC'})
# 데이터수집
scheduler.add_job(func=crawling.crawling_new, trigger='interval', days=1)
# 데이터적재
scheduler.add_job(func=postgre_DB.new_to_db, trigger = 'interval', days=1)
# 데이터 추출 및 모델링
scheduler.add_job(func = modeling, trigger= 'interval', days=1)

scheduler.start()


# 웹서비스
if __name__ == "__main__":
  app = create_app()
  app.run()
