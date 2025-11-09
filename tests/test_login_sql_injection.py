
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_should_not_allow_sql_injection():
    # Ожидаем, что вход с username, содержащим SQL-комментарий, должен БЫТЬ запрещён.
    # В текущем состоянии приложения тест упадёт (и это нормально до S06).
    payload = {"username": "admin'-- ", "password": "x"}
    resp = client.post("/login", json=payload)
    assert resp.status_code == 401, "SQLi-бэйпас логина должен быть закрыт"

def test_login_positive_correct_credentials():
    """Проверяет, что пользователь с корректными данными может успешно войти в систему."""
    # Используем учетные данные, которые создаются в scripts/init_db.py
    payload = {"username": "admin", "password": "admin"}
    response = client.post("/login", json=payload)

    # Ожидаем успешный ответ
    assert response.status_code == 200

    # Проверяем, что в ответе есть токен
    response_data = response.json()
    assert "token" in response_data
    assert response_data["token"] is not None