from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to ACEest Fitness & Gym!" in response.data

def test_members():
    client = app.test_client()
    response = client.get("/members")
    assert response.status_code == 200

def test_plans():
    client = app.test_client()
    response = client.get("/plans")
    assert response.status_code == 200