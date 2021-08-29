
""" Тест создания экземпляра класса Barrel """

import random
from pytest import fixture
from loto_classes import config, Barrel

TEST_NUMBER = random.randint(1, config.BARRELS_IN_SACK)


@fixture(scope="module")
def barrel():
    """Фикстура с экземляром класса Barrel"""
    return Barrel(TEST_NUMBER)


def test_repr(barrel):
    """Тест структуры класса Barrel, тест __repr__"""
    assert barrel.__repr__() == f"({TEST_NUMBER})"


def test_number(barrel):
    """Тест свойства number класса Barrel"""
    assert barrel.number == TEST_NUMBER
