import pytest
from Sportsman import Sportsman




@pytest.mark.parametrize('answer',[7,6,12,23])
def test_run(answer):
    assert Sportsman.run(60) == answer

@pytest.mark.parametrize('answer',[5,3,10,6])
def test_jump(answer):
    assert Sportsman.jump("from the spot") == answer

@pytest.mark.parametrize('answer',[8,9,10,11])
def test_sleep(answer):
    assert Sportsman.sleep(answer) == "I recovered"

@pytest.mark.parametrize('answer',["steroids",7,"eat",10])
def test_eat(answer):
    assert Sportsman.eat(answer) == "zaebumba"