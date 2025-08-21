from dotenv import load_dotenv
import pytest
import requests
import os

load_dotenv()

API_KEY = os.getenv("YOU_GILE_API_KEY")
if not API_KEY:
    raise ValueError("YOU_GILE_API_KEY не установлена!")

BASE_URL = "https://ru.yougile.com/api-v2"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def headers():
    return HEADERS


@pytest.fixture
def create_temp_project(base_url, headers):
    """Создаём временный проект и возвращаем его ID"""
    project_data = {"title": "Test Project (pytest)"}  # ✅ Принимается API
    response = requests.post(
        f"{base_url}/projects", json=project_data, headers=headers
    )

    assert response.status_code in [
        200,
        201,
    ], f"Ошибка создания: {response.status_code}, {response.text}"
    response_json = response.json()

    # Извлекаем ID
    project_id = response_json.get("data", {}).get("id") or response_json.get(
        "id"
    )
    assert project_id, "Не удалось получить ID проекта из ответа"

    yield project_id

    # Очистка
    try:
        requests.delete(f"{base_url}/projects/{project_id}", headers=headers)
    except Exception as e:
        print(f"Не удалось удалить проект {project_id}: {e}")
