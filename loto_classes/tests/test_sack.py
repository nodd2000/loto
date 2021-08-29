
""" Тест создания экземпляра класса Sack """

from pytest import fixture
from loto_classes import config, Sack, Barrel


@fixture(scope="module")
def sack():
    """Фикстура с экземляром класса Sack"""
    return Sack()


def test_repr(sack):
    """Тест структуры класса Sack, тест __repr__"""
    a = eval(sack.__repr__())
    assert isinstance(a, list)
    assert len(a) == config.BARRELS_IN_SACK


def test_pull_barrel(sack):
    """Тест метода pull_barrel() класса Sack"""
    len_before = len(sack)
    pulled = sack.pull_barrel()
    assert isinstance(pulled, Barrel)
    assert (len_before - 1) == len(sack)
    for i in range(len(sack)):
        sack.pull_barrel()
    assert len(sack) == 0
