
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_echo_should_escape_script_tags():
    resp = client.get("/echo", params={"msg": "<script>alert(1)</script>"})
    # В защищённом варианте скрипт не должен оказаться в ответе как тег.
    assert "<script>" not in resp.text, "Вывод должен экранировать потенциальную XSS-последовательность"

def test_echo_positive_simple_message():
    """Проверяет, что /echo корректно отображает простое сообщение."""
    message = "Hello, World!"
    response = client.get("/echo", params={"msg": message})

    assert response.status_code == 200
    # Проверяем, что сообщение присутствует в теле ответа
    assert message in response.text