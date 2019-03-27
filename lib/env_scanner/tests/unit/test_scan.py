import pytest
from env_scanner.scan import list_contents, list_envs, find_pkg
from env_scanner.tests.prod_env_contents import OS40 #OS41 OS42 OS42_LEGACY


class TestListContentDevelopment():
    """
    This is to check that the constant set of development environments
    always returns a set of values.  The values change constantly, along with
    the number of values (packages), so it's currently quite hard to check
    them against a specific set of packages, but that may change in the
    future if we can reduce the set down to just SciTools packages once the
    use of pip takes off.

    """
    def test_experimental_current(self):
        result = list_contents('scitools/experimental-current')
        print(list_contents)
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
        result = list_contents('scitools/default-previous')
        assert len(result) > 0

    def test_default_legacy_previous(self):
        result = list_contents('scitools/default_legacy-previous')
        assert len(result) > 0


class TestListContentsProduction():
    """
    This is to test that list_contents for production environments always
    returns a set of values.

    Due to the immutable nature of production environments, this group of
    tests can be a little more specific, and check the package list returned
    against a full set of known packages, but this means another test will
    need to be added with each new production environment created.

    """
    # def setup(self):
    # # TODO: Write method for dissecting source repo manifest to match the list_contents function output




    def test_os40_1(self):
        OS40_munged =
        expected = OS40_munged
        result = list_contents('scitools/default_legacy-previous')
        assert result == expected


# class TestListEnvs():
#     def test_list(self):




if __name__ == '__main__':
    pytest.main()
