from fastapi.testclient import TestClient
from fast_api import app

client = TestClient(app)


# Functional testing for incorrect HTTP method | We have a post method in FastApi and we are testing for get request
def test_read_predict():
    response = client.get("/predict")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


# Functional testing for correct input
def test_predict_clean_input():
    response = client.post("/predict", json={"text": "ok"})
    assert response.status_code == 200
    assert response.json() == {"probabilities": {"negative": 0.00012119442544644699, "neutral": 0.9994199275970459,
                                                 "positive": 0.00045894348295405507}, "sentiment": "neutral",
                               "confidence": 0.9994199275970459}


# Functional testing for empty input
def test_predict_bad_input():
    response = client.post("/predict", json={})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [{"loc": ["body", "text"], "msg": "field required", "type": "value_error.missing"}]}
