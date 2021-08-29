
""" Тест создания экземпляра класса Game """

import random
from pytest import fixture
from unittest import mock
from loto_classes import config, Game


@fixture(scope="module")
def game_comp():
    """Фикстура с экземляром класса Game c игроками типа COMP"""
    test_players_num = random.randint(config.MIN_NUM_PLAYERS, config.MAX_NUM_PLAYERS)
    test_players = [{"id": i,
                     "name": config.COMP_NAME.format(i),
                     "type": config.COMPUTER_TYPE_ID} for i in range(test_players_num)]
    return Game(test_players)


@fixture(scope="module")
def game_human():
    """Фикстура с экземляром класса Game c игроками типа HUMAN"""
    test_players_num = random.randint(config.MIN_NUM_PLAYERS, config.MAX_NUM_PLAYERS)
    test_players = [{"id": i,
                     "name": config.HUMAN_NAME.format(i),
                     "type": config.HUMAN_TYPE_ID} for i in range(test_players_num)]
    return Game(test_players)


@fixture(scope="module")
def game_mix():
    """Фикстура с экземляром класса Game cо смешанными игроками"""
    test_players_num = random.randint(config.MIN_NUM_PLAYERS, config.MAX_NUM_PLAYERS)
    random_type = random.choice([config.HUMAN_TYPE_ID, config.COMPUTER_TYPE_ID])
    test_players = [{"id": i,
                     "name": (config.COMP_NAME.format(i) if random_type == config.COMPUTER_TYPE_ID
                              else config.HUMAN_NAME.format(i)),
                     "type": random_type} for i in range(test_players_num)]
    return Game(test_players)


@fixture(scope="module", params=['game_comp', 'game_human', 'game_mix'])
def game(request):
    """Parametrized фикстура с экземляром класса Game"""
    return request.getfixturevalue(request.param)


@mock.patch('loto_classes.user_input.ask_player_act', autospec=True)
def test_play(mocked_ask_player_act, game):
    """Тест метода play() класса Game: создает новую игру и проигрывает ее. Тестируются все классы"""
    mocked_ask_player_act.return_value = random.choice([config.ANSWER_TYPES.get(False),
                                                        config.ANSWER_TYPES.get(True)])
    game_result = game.play()
    assert game_result.get("round") >= 1
    assert game_result.get("winner") is not None