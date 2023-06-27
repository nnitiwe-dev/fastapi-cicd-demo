import pytest
from fastapi.testclient import TestClient
from app.main import app



def test_get_tweets():
    client = TestClient(app)
    response = client.get("/tweets")
    print(response)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10
    for tweet in data:
        #Very basic test of the data generated from Twitter
        assert "user" in tweet
        assert "date_created" in tweet
        assert "num_likes" in tweet
        assert "source" in tweet
        assert "content" in tweet
        assert "sentiment" in tweet
        assert "polarity" in tweet
        assert isinstance(tweet["user"], str)
        assert isinstance(tweet["date_created"], str)
        assert isinstance(tweet["num_likes"], int)
        assert isinstance(tweet["source"], str)
        assert isinstance(tweet["content"], str)
        assert isinstance(tweet["sentiment"], str)
        assert isinstance(tweet["polarity"], float)

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client
