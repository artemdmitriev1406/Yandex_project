# Артём Дмитриев, 49-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request


# Клиент создает заказ, и по треку заказа можно получить данные о заказе
def test_get_order_by_track_returns_200():
    # Выполнить запрос на создание заказа
    create_response = sender_stand_request.post_new_order(data.order_body)
    assert create_response.status_code == 201, create_response.text

    # Сохранить номер трека заказа
    track = create_response.json()["track"]

    # Выполнить запрос на получение заказа по треку заказа
    get_response = sender_stand_request.get_order_by_track(track)

    # Проверить, что код ответа равен 200
    assert get_response.status_code == 200, get_response.text
