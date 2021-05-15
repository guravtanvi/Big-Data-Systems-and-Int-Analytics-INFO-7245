from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_read_item():
    response = client.get("/all", headers={"access_token": "1234567asdfgh"})
    assert response.status_code == 200
    assert response.json() == {
    "data": [
    [
      9700,
      " 36 months",
      17.86,
      350,
      "D",
      "D5",
      "teacher",
      "2 years",
      "OWN",
      27000,
      "Verified",
      "May-2015",
      "Fully Paid",
      "home_improvement",
      "Home improvement",
      14.67,
      "Apr-2003",
      2,
      0,
      0,
      0,
      20,
      "f",
      "INDIVIDUAL",
      1,
      0,
      "850 Castaneda Centers\nSouth Matthewberg, CT 70466"
    ]
  ]
}


def test_read_all_bad_token():
  response = client.get("/all", headers={"access_token": "12345"})
  assert response.status_code == 403
  assert response.json() == {"detail": "Could not validate credentials"}

def test_verification_status_bad_token():
  response = client.get("/verification_details/Verified", headers={"access_token": "1234567"})
  assert response.status_code == 403
  assert response.json() == {"detail": "Could not validate credentials"}


def test_read_inexistent_item():
  response = client.get("/verification_details/Verify", headers={"access_token": "1234567asdfgh"})
  assert response.status_code == 404
  assert response.json() == {"detail": "Item not found"}

