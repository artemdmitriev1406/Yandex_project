# Артём Дмитриев, 49-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


# Проверка: заказ можно получить по номеру трека, код ответа 200
def test_get_order_by_track_returns_200():
    # Создать заказ и сохранить номер трека
    track = sender_stand_request.get_new_order_track()

    # Выполнить запрос на получение заказа по треку
    response = sender_stand_request.get_order_by_track(track)

    # Проверить, что код ответа равен 200
    assert response.status_code == 200