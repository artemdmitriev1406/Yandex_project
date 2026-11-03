import requests

import configuration
import data


# Создание заказа: POST /api/v1/orders
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


# Получение заказа по номеру трека: GET /api/v1/orders/track?t=<трек>
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                        params={"t": track})
