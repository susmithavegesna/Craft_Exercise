import pytest
from api_template.app import application


@pytest.fixture()
def test_client():
    """Test healthy response from example"""
    flask_app = application()
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client


def test_health(test_client):
    response = test_client.get('/healthcheck')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


