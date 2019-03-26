import pytest
from env_scanner.scan import list_contents, list_envs, find_pkg


class TestListContent():
    def test_experimental_current(self):
        result = list_contents('scitools/experimental-current')
        assert len(result) > 0

    def test_experimental_legacy_current(self):
        result = list_contents('scitools/experimental_legacy-current')
        assert len(result) > 0

    def test_default_next(self):
        result = list_contents('scitools/default-next')
        assert len(result) > 0

    def test_default_legacy_next(self):
        result = list_contents('scitools/default_legacy-next')
        assert len(result) > 0

    def test_default_current(self):
        result = list_contents('scitools/default-current')
        assert len(result) > 0

    def test_default_legacy_current(self):
        result = list_contents('scitools/default_legacy-current')
        assert len(result) > 0

    def test_default_previous(self):
        result = list_contents('scitools/default_previous')
        assert len(result) > 0

    def test_default_legacy_previous(self):
        result = list_contents('scitools/default_legacy-previous')
        assert len(result) > 0

if __name__ == '__main__':
    pytest.main()
