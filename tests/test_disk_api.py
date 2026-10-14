BASE_URL = "https://cloud-api.yandex.net/v1/disk"


def test_get_resource(api, folder):
    """get /v1/disk/resources"""
    response = api.get(f"{BASE_URL}/resources", params={"path": folder})
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "dir"
    assert data["path"] == folder


def test_put_create_folder(api, unique_path):
    """put /v1/disk/resources"""
    path = unique_path("put-folder")
    response = api.put(f"{BASE_URL}/resources", params={"path": path})
    assert response.status_code == 201


def test_post_copy_resource(api, folder, unique_path):
    """post /v1/disk/resources/copy"""
    target = unique_path("post-dst")
    response = api.post(
        f"{BASE_URL}/resources/copy",
        params={"from": folder, "path": target},
    )
    assert response.status_code in (201, 202)


def test_delete_folder(api, folder):
    """delete /v1/disk/resources"""
    response = api.delete(
        f"{BASE_URL}/resources",
        params={"path": folder, "permanently": "true"},
    )
    assert response.status_code in (202, 204)
