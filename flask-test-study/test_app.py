import pytest
import json
from app import create_app


@pytest.fixture
def api():
    app = create_app()
    app.config['TESTING'] = True
    api = app.test_client()

    return api


def test_ping(api):
    response = api.get('/ping')
    assert b'pong' in response.data


def test_hello(api):
    response = api.post(
        '/hello',
        data=json.dumps({'name': 'hs'}),
        content_type='application/json'
    )
    hello = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert hello == {
        "message": "hello, hs"
    }
