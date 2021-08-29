
"""Тесты на парсеры user input"""

from pytest import fixture
from loto_classes import user_input, config


@fixture(scope="module", params=[
    ('-1', None),
    ('0', None),
    ('1', None),
    ('2', 2),
    ('3', 3),
    ('8', 8),
    ('9', None),
    (' ', None)
])
def fixture_players_num(request):
    return request.param


@fixture(scope="module", params=[
    ('ч', config.HUMAN_TYPE_ID),
    ('Ч', config.HUMAN_TYPE_ID),
    ('h', config.HUMAN_TYPE_ID),
    ('H', config.HUMAN_TYPE_ID),
    ('к', config.COMPUTER_TYPE_ID),
    ('К', config.COMPUTER_TYPE_ID),
    ('c', config.COMPUTER_TYPE_ID),
    ('C', config.COMPUTER_TYPE_ID),
    ('f', None),
    ('m f f', None),
    (' ', None),
    ('f', None)
])
def fixture_player_type(request):
    return request.param


@fixture(scope="module", params=[
    ('д', True),
    ('Д', True),
    ('y', True),
    ('Y', True),
    ('н', False),
    ('Н', False),
    ('n', False),
    ('N', False),
    (' ', None),
    ('нет', None),
    ('d d l', None),
    ('no!', None),
])
def fixture_answer_type(request):
    return request.param


def test_parse_players_num(fixture_players_num):
    (text, result) = fixture_players_num
    assert user_input.parse_players_num(text) == result


def test_parse_player_type(fixture_player_type):
    (text, result) = fixture_player_type
    assert user_input.parse_player_type(text) == result


def test_parse_player_act(fixture_answer_type):
    (text, result) = fixture_answer_type
    assert user_input.parse_player_act(text) == result


def test_parse_new_game(fixture_answer_type):
    (text, result) = fixture_answer_type
    assert user_input.parse_new_game(text) == result
