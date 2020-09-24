
import datetime
import json
import requests

from flask import Flask, jsonify
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api


def create_app(CONFIG_FILE):
  app = Flask(__name__)
  api = Api(app)

  app.config.from_object(CONFIG_FILE)

  from .models import db
  db.init_app(app)

  migrate = Migrate(app, db)

  manager = Manager(app)
  manager.add_command('db', MigrateCommand)

  from app.urls import create_urls
  create_urls(app, api)

  return manager
