import pytest
from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

initial_feedback_email = "kubilk56@gmail.com"
initial_feedback_rating = 3
changed_feedback_rating = 5


@pytest.mark.dependency()
def test_create_feedback(request):
    response = client.post(
        "/feeadback/create",
        json={"email": initial_feedback_email, "rating": initial_feedback_rating},
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["email"] == "kubilk56@gmail.com"
    assert response.json()["rating"] == 3
    request.config.cache.set("email", response.json()["email"])


@pytest.mark.dependency(depends=["test_create_feedback"])
def test_get_all_feedback():
    response = client.get("/feedback/list/all")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() is not None


@pytest.mark.dependency(depends=["test_create_feedback"])
def test_get_one_feedback(request):
    email = request.config.cache.get("email", None)
    response = client.get(f"/feedback/get/{id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["email"] == email
    assert response.json()["rating"] == initial_feedback_rating
    assert (
        response.json()["description"] == initial_feedback_rating
        or changed_feedback_rating
    )


@pytest.mark.dependency(depends=["test_create_feedback", "test_get_one_feedback"])
def test_patch_feedback(request):
    email = request.config.cache.get("email", None)
    response = client.patch(
        "/feedback/update",
        json={
            "email": email,
            "rating": initial_feedback_rating,
            "change_rating": changed_feedback_rating,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["email"] == email
    assert response.json()["rating"] == initial_feedback_rating
    assert response.json()["change_rating"] == changed_feedback_rating


@pytest.mark.dependency(
    depends=[
        "test_create_feedback",
        "test_get_one_feedback",
        "test_patch_feedback",
        "test_get_all_feedback",
    ]
)
def test_delete_feedback(request):
    email = request.config.cache.get("email", None)
    response = client.delete("/feedback/delete",
        json={
            "email": email,
        })
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["description"] == "Feedback Deleted"
