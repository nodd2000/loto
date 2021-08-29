
from loto_classes import player, sack, config


class Game:
    def __init__(self, players_dict):
        self._players = self._create_players(players_dict)
        self._sack = sack.Sack()
        self._round = 0

    @staticmethod
    def _create_players(players_dict):
        players = list()
        for player_dict in players_dict:
            players.append(player.Player(player_dict.get("id"), player_dict.get("name"), player_dict.get("type")))
        return players

    def _kick_player(self, player_):
        if player_ in self._players:
            self._players.remove(player_)

    def _show_all_players(self):
        for player_ in self._players:
            print(player_)

    def _find_winner(self, player_, to_kick):
        """Impure"""
        winner = None
        if len(self._players) - len(to_kick) < config.MIN_NUM_PLAYERS:
            for player__ in to_kick:
                self._kick_player(player__)
            winner = self._players[0]
        if player_.check_win():
            winner = player_
        return winner

    def _inc_round(self):
        self._round += 1
        print(config.NEXT_ROUND.format(self._round))
        return self._round

    def _pull_barrel(self):
        barrel = self._sack.pull_barrel()
        print(config.NEXT_BARREL.format(barrel))
        print(config.IN_SACK.format(len(self._sack)))
        return barrel

    @staticmethod
    def _ask_player_for_act(player, barrel):
        print(config.ACT_PLAYER.format(player.name, barrel))
        answer = player.act(barrel)
        return answer

    @staticmethod
    def _is_correct_answer(player_, barrel, answer):
        if answer == (barrel.number in player_.card.numbers_on_card):
            return True
        if answer:
            print(config.WRONG_ACT_TRUE.format(player_.name))
        else:
            print(config.WRONG_ACT_FALSE.format(player_.name))
        return False

    def _next_round(self):
        self._inc_round()
        barrel = self._pull_barrel()
        self._show_all_players()
        to_kick = []
        winner = None
        for player_ in self._players:
            answer = self._ask_player_for_act(player_, barrel)

            if not self._is_correct_answer(player_, barrel, answer):
                print(config.LOSER.format(player_.name))
                to_kick.append(player_)

            winner = self._find_winner(player_, to_kick)

            if winner is not None:
                print(config.WINNER.format(winner.name))
                break

        for player_ in to_kick:
            self._kick_player(player_)

        return winner

    def play(self):
        winner = None
        while winner is None:
            winner = self._next_round()
        print(config.END_GAME.format(self._round))
        return {"winner": winner, "round": self._round}

    @property
    def players(self):
        return self._players
