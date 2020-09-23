import datetime

from utils.data import response_header, list_products
from app import db

from flask import jsonify, request, make_response
from flask.views import MethodView
from flask_restful import Resource, Api, fields, marshal_with

from app.models.product import Product as ProductModel


resource_field = {
    "product_id": fields.Integer,
    "product_name": fields.String,
    "price": fields.Float
}


class ProductList(Resource):
    @marshal_with(resource_field)
    def get(self, ):
        products = ProductModel.query.all()
        print(ProductModel.query.all())
        return products

    @marshal_with(resource_field)
    def post(self, ):
        new_product = ProductModel(
            product_name=request.json['product_name'],
            price=request.json['price']
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product, 201 

class Product(Resource):
    @marshal_with(resource_field)
    def get(self, product_id):
        product = ProductModel.query.filter_by(product_id=product_id).first()
        return product

    @marshal_with(resource_field)
    def put(self, product_id):
        product_update = ProductModel.query.filter_by(product_id=product_id).first()
        product_update.product_name = request.json['product_name']
        product_update.price = request.json['price']
        db.session.commit()
        return product_update

    def delete(self, product_id):
        product_delete = ProductModel.query.filter_by(product_id=product_id).first()
        db.session.delete(product_delete)
        db.session.commit()
        return '', 204




def response_header(data):
    return jsonify({
        "date": datetime.datetime.now(),
        "quantity_total": len(list_products),
        "results": data
    })

class ProductKabum(MethodView):
    def get(self, codigo):
        if codigo == None:
            return response_header(list_products)
        else:
            for product in list_products:
                if product['codigo'] == codigo:
                    return response_header(product)

    def post(self, ):
        pass

    def put(self, codigo):
        pass

    def patch(self, codigo):
        pass

    def delete(self, codigo):
        for product in list_products:
            if product['codigo'] == codigo:
                list_products.remove(product)

        return '', 204
