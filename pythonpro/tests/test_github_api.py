from unittest.mock import Mock
import pytest
from pythonpro import api_git_hub


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars3.githubusercontent.com/u/63620799?v=4'
    resp_mock.json.return_value = {'login': 'Alfareiza', 'id': 63620799,
                                   'avatar_url': url}
    get_original = api_git_hub.requests.get
    api_git_hub.requests.get = Mock(return_value=resp_mock)
    yield url
    api_git_hub.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = api_git_hub.get_avatar('Alfareiza')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = api_git_hub.get_avatar('renzon')
    assert 'https://avatars3.githubusercontent.com/u/3457115?v=4' == url
