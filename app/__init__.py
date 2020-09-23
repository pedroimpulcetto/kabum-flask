
import datetime
import json
import requests

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

app.config.from_object('config')


db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models.product import Product
from app.controllers.product_controller import ProductList as ProductListController
from app.controllers.product_controller import Product as ProductController
from app.controllers.product_controller import ProductKabum as ProductKabumController

# UTILIZANDO flask_restful 
api.add_resource(ProductListController, '/')
api.add_resource(ProductController, '/<int:product_id>')


# UTILIZANDO flask.views.MethodView
view = ProductKabumController.as_view('products')
app.add_url_rule('/kabum', defaults={'codigo': None},
                 view_func=view, methods=['GET', 'POST',])
app.add_url_rule('/', view_func=view, methods=['POST',])
app.add_url_rule('/kabum/<int:codigo>', view_func=view,
                 methods=['GET', 'PUT', 'DELETE', ])
