import os
import uuid
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://cloud-api.yandex.net/v1/disk"


@pytest.fixture(scope="session")
def token():
    value = os.getenv("YANDEX_DISK_TOKEN")
    if not value:
        pytest.fail("Fill YANDEX_DISK_TOKEN variable in .env")
    return value

@pytest.fixture(scope="session")
def api(token):
    session = requests.Session()
    session.headers.update({"Authorization": f"OAuth {token}"})
    return session

@pytest.fixture
def unique_path(api):
    paths = []
    def _make(prefix="api-test"):
        path = f"disk:/{prefix}-{uuid.uuid4().hex[:8]}"
        paths.append(path)
        return path
    yield _make
    for path in reversed(paths):
        api.delete(f"{BASE_URL}/resources",params={"path": path, "permanently": "true"},)

@pytest.fixture
def folder(api, unique_path):
    path = unique_path("folder")
    response = api.put(f"{BASE_URL}/resources", params={"path": path})
    assert response.status_code == 201, response.text
    return path
