import pytest

@pytest.fixture(scope="module")
def preSetupWork():
    print("I set up browser instance")