
""" Тест создания экземпляров класса Player """

from pytest import fixture
from loto_classes import config, Player

TEST_PLAYER_ID1 = 1
TEST_PLAYER_NAME1 = 'TEST1'
TEST_PLAYER_TYPE1 = config.HUMAN_TYPE_ID
TEST_PLAYER_ID2 = 2
TEST_PLAYER_NAME2 = 'TEST2'
TEST_PLAYER_TYPE2 = config.COMPUTER_TYPE_ID


@fixture(scope="module")
def player_human():
    """Фикстура с экземляром класса Player типа Human"""
    return Player(TEST_PLAYER_ID1, TEST_PLAYER_NAME1, TEST_PLAYER_TYPE1)


@fixture(scope="module")
def player_computer():
    """Фикстура с экземляром класса Player типа Computer"""
    return Player(TEST_PLAYER_ID2, TEST_PLAYER_NAME2, TEST_PLAYER_TYPE2)


@fixture(scope="module", params=['player_human', 'player_computer'])
def player(request):
    """Parametrized фикстура с экземляром класса Player"""
    return request.getfixturevalue(request.param)


def test_id(player):
    """Тест свойства id класса Player"""
    assert player.id in [TEST_PLAYER_ID1, TEST_PLAYER_ID2]


def test_name(player):
    """Тест свойства name класса Player"""
    assert player.name in [TEST_PLAYER_NAME1, TEST_PLAYER_NAME2]
