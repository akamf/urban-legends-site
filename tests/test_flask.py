import pytest
from app.app import init_app

# os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
@pytest.fixture
def test_app():
    return init_app()

def test_post_not_allowed(test_app):
    with test_app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 405

def test_index(test_app):
    with test_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'Urban Legends' in response.data

def test_submit_get(test_app):
    with test_app.test_client() as test_client:
        response = test_client.get('/legends-unveild/the-game/rules')
        assert response.status_code == 200
        assert b'Legends Unveiled' in response.data
        