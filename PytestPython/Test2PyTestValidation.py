#Fixtures
import pytest


@pytest.fixture(scope="function")
def preSetupWork():
    print("I set up browser instance")

def test_thirdCheck(preSetupWork):
    print("This is Third test")
