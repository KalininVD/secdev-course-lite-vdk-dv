
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_should_not_return_all_on_injection():
    # По бессмысленному запросу ожидаем 0, а по инъекции — тоже 0 (не все элементы)
    resp_noise = client.get("/search", params={"q": "zzzzzzzzz"}).json()
    inj = client.get("/search", params={"q": "' OR '1'='1"}).json()
    assert len(inj["items"]) <= len(resp_noise["items"]), "Инъекция в LIKE не должна приводить к выдаче всех элементов"

def test_search_positive_finds_item():
    """Проверяет, что поиск по существующему слову возвращает релевантный результат."""
    # 'apple' точно есть в базе данных
    response = client.get("/search", params={"q": "apple"})
    
    assert response.status_code == 200
    
    response_data = response.json()
    assert len(response_data["items"]) > 0
    # Проверяем, что в найденных товарах действительно есть 'apple'
    assert any("apple" in item["name"] for item in response_data["items"])