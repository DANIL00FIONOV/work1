import pytest
from Champ import Champ


@pytest.mark.parametrize('answer',[7,5,12,23])
def test_run(answer):
    assert Champ.run(60) == answer

@pytest.mark.parametrize('answer',[5,3,10,6])
def test_jump(answer):
    assert Champ.jump("from the spot") == answer