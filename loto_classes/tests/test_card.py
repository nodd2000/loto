
""" Тест создания экземпляра класса Card """

import random
from pytest import fixture
from loto_classes import config, Card, Barrel


@fixture(scope="module")
def card():
    """Фикстура с экземляром класса Card"""
    return Card()


def test_repr(card):
    """Тест структуры класса Card, тест __repr__"""
    a = eval(card.__repr__())
    assert isinstance(a, list)
    assert len(a) == config.CARD_COLUMNS
    assert isinstance(a[0], list)
    assert len(a[0]) == 2
    assert isinstance(a[0][0], list)
    assert len(a[0][0]) == config.NUMBERS_ON_ROW
    assert isinstance(a[0][0][0], int)


def test_numbers_on_card(card):
    """Тест свойства numbers_on_card класса Card"""
    assert isinstance(card.numbers_on_card, list)
    assert len(card.numbers_on_card) == config.CARD_COLUMNS * config.NUMBERS_ON_ROW
    assert isinstance(card.numbers_on_card[0], int)


def test_covered_numbers(card):
    """Тест метода cover_card_cell() класса Card"""
    card.cover_card_cell(Barrel(card.numbers_on_card[0]))
    number = random.randint(config.MIN_BARREL_NUMBER, config.BARRELS_IN_SACK)
    while number in card.numbers_on_card:
        number = random.randint(config.MIN_BARREL_NUMBER, config.BARRELS_IN_SACK)
    card.cover_card_cell(Barrel(number))
    assert card.covered_numbers == [card.numbers_on_card[0]]
