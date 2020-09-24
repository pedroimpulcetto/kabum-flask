from app.models.product import Product
from app.controllers.product_controller import ProductList as ProductListController
from app.controllers.product_controller import Product as ProductController
from app.controllers.product_controller import ProductKabum as ProductKabumController


def create_urls(app, api):
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