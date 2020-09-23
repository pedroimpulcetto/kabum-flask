import datetime
import json
import requests

from flask import jsonify

products = [
    '85197',
    '79936',
    '87400'
]

list_products = []

for p in products:
    r = requests.get(
        f'https://servicespub.prod.api.aws.grupokabum.com.br/descricao/v1/descricao/produto/{p}')
    product = json.loads(r.content)
    list_products.append(product)


def response_header(data):
    return jsonify({
        "date": datetime.datetime.now(),
        "quantity_total": len(list_products),
        "results": data
    })
