import pytest
from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

initial_feedback_id=1
initial_feedback_email = "kubilk56@gmail.com"
initial_feedback_rating = 3
changed_feedback_rating = 5


@pytest.mark.dependency()
def test_create_feedback(request):
    response = client.post(
        "/feedback/create",
        json={"email": initial_feedback_email, "rating": initial_feedback_rating},
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["email"] == initial_feedback_email
    assert response.json()["rating"] == initial_feedback_rating
    request.config.cache.set("feedback_id", initial_feedback_id)


@pytest.mark.dependency(depends=["test_create_feedback"])
def test_get_all_feedback():
    response = client.get("/feedback/list/all")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() is not None


@pytest.mark.dependency(depends=["test_create_feedback"])
def test_get_one_feedback(request):
    feedback_id = request.config.cache.get("feedback_id", None)
    response = client.get(f"/feedback/get/{feedback_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == feedback_id
    assert response.json()["email"] == initial_feedback_email


@pytest.mark.dependency(depends=["test_create_feedback", "test_get_one_feedback"])
def test_patch_feedback(request):
    id = request.config.cache.get("feedback_id", None)
    response = client.patch(
        "/feedback/update",
        json={
            "id":id,
            "email": initial_feedback_email,
            "rating": initial_feedback_rating
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == id
    assert response.json()["email"] == initial_feedback_email
    assert response.json()["rating"] == initial_feedback_rating


@pytest.mark.dependency(
    depends=[
        "test_create_feedback",
        "test_get_one_feedback",
        "test_patch_feedback",
        "test_get_all_feedback",
    ]
)
def test_delete_feedback(request):
    id = request.config.cache.get("feedback_id", None)
    #this comment is to keep the master sample data is still exist
    #response = client.delete("/feedback/delete",
    #    json={
    #        "id":id
    #    })
    
    #assert response.status_code == status.HTTP_200_OK
    #assert response.json()["detail"] == "Feedback Deleted"
