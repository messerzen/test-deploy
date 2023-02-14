import sys
sys.path.append("C:/git/testing-integriry/project")
from project.main.main import mySum


def test_sum():
    assert mySum(4,5) == 9