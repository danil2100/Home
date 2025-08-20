import pytest
import requests
import os


class TestYouGileProjects:

    def test_create_project_positive(self, base_url, headers):
        """Позитивный: создание проекта"""
        expected_title = f"New Project {os.urandom(4).hex()}"
        project_data = {
            "title": expected_title
     }

        response = requests.post(f"{base_url}/projects", json=project_data, headers=headers)
        print(f"Create response: {response.status_code}, {response.text}")

        assert response.status_code in [200, 201], f"Ошибка: {response.status_code}, {response.text}"
        response_json = response.json()
        data = response_json.get("data") or response_json

        assert "id" in data, "В ответе нет 'id'"

        project_id = data["id"]
        get_response = requests.get(f"{base_url}/projects/{project_id}", headers=headers)
        assert get_response.status_code == 200, f"Не удалось получить проект: {get_response.text}"
        get_data = get_response.json().get("data") or get_response.json()

        assert get_data.get("name") == expected_title or get_data.get("title") == expected_title, \
            f"Ожидалось название = {expected_title}, получено: {get_data}"

        requests.delete(f"{base_url}/projects/{project_id}", headers=headers)
        
    def test_create_project_negative_empty_title(self, base_url, headers):
        """Негативный: создание без title"""
        project_data = {}  

        response = requests.post(f"{base_url}/projects", json=project_data, headers=headers)
        print(f"Empty title response: {response.status_code}, {response.text}")

        assert response.status_code == 400, f"Ожидался 400, получен: {response.status_code}"
        error_data = response.json()
        assert "title" in str(error_data).lower() or "required" in str(error_data).lower()

    def test_get_project_positive(self, base_url, headers, create_temp_project):
        """Позитивный: получение проекта по ID"""
        project_id = create_temp_project

        response = requests.get(f"{base_url}/projects/{project_id}", headers=headers)
        print(f"Get response: {response.status_code}, {response.text}")

        assert response.status_code == 200, f"Ошибка: {response.status_code}, {response.text}"
        response_json = response.json()
        data = response_json.get("data") or response_json
        assert data["id"] == project_id
        assert "title" in data  

    def test_get_project_negative_invalid_id(self, base_url, headers):
        """Негативный: получение по несуществующему ID"""
        invalid_id = "00000000-0000-0000-0000-000000000000"

        response = requests.get(f"{base_url}/projects/{invalid_id}", headers=headers)
        print(f"Invalid ID response: {response.status_code}, {response.text}")

        assert response.status_code in [400, 404], f"Ожидался 400 или 404, получен: {response.status_code}"

    def test_update_project_positive(self, base_url, headers, create_temp_project):
        """Позитивный: обновление проекта"""
        project_id = create_temp_project
        new_title = f"Updated Project {os.urandom(4).hex()}"

        updated_data = {"title": new_title}

        response = requests.put(f"{base_url}/projects/{project_id}", json=updated_data, headers=headers)
        print(f"Update response: {response.status_code}, {response.text}")

        assert response.status_code == 200, f"Ошибка: {response.status_code}, {response.text}"

        get_response = requests.get(f"{base_url}/projects/{project_id}", headers=headers)
        assert get_response.status_code == 200
        get_data = get_response.json().get("data") or get_response.json()

        assert get_data.get("name") == new_title or get_data.get("title") == new_title, \
            f"Ожидалось название = {new_title}, получено: {get_data}"


    def test_update_project_negative_invalid_title(self, base_url, headers, create_temp_project):
        """Негативный: обновление с пустым title"""
        project_id = create_temp_project

        # Сохраняем старое состояние
        old_response = requests.get(f"{base_url}/projects/{project_id}", headers=headers)
        assert old_response.status_code == 200
        old_data = (old_response.json().get("data") or old_response.json())

        # Пытаемся обновить
        invalid_data = {"title": ""}
        response = requests.put(f"{base_url}/projects/{project_id}", json=invalid_data, headers=headers)
        print(f"Invalid update response: {response.status_code}, {response.text}")

        if response.status_code == 400:
            error_data = response.json()
            assert "title" in str(error_data).lower() or "validation" in str(error_data).lower()
        elif response.status_code == 200:
            new_response = requests.get(f"{base_url}/projects/{project_id}", headers=headers)
            new_data = (new_response.json().get("data") or new_response.json())
            assert new_data["title"] == old_data["title"], "Title изменился на пустое значение!"
        else:
            pytest.fail(f"Неожиданный статус: {response.status_code}")