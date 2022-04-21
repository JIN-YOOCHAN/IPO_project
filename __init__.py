import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import crawling
import postgre_DB
import modeling
from flask_app import flask_init

flask_init.create_app()