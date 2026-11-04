import requests

import configuration
import data


# Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


# Создание заказа и получение номера его трека
def get_new_order_track():
    response = post_new_order(data.order_body)
    return response.json()["track"]


# Получение заказа по номеру трека
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                        params={"t": track})