from loto_classes import card, config, user_input


class Player:
    def __init__(self, player_id, player_name, player_type):
        self._card = card.Card()
        self._name = player_name
        self._id = player_id
        self._type = player_type
        self._answer = False

    def __str__(self):
        player_look = config.CARD_NAME.format(self._name) + '\n' + self._card.__str__()
        return player_look

    def __repr__(self):
        return f"{self._id}"

    def _act_computer(self, barrel):
        answer = barrel.number in self._card.numbers_on_card
        print(answer)
        return answer

    def _act_human(self):
        return user_input.ask_player_act(self._name)

    def act(self, barrel):
        """Impure: deterministic but with side effects (cover_card_cell)"""
        if self._type == config.HUMAN_TYPE_ID:
            answer = self._act_human()
        else:
            answer = self._act_computer(barrel)
        if answer:
            self._card.cover_card_cell(barrel)
        return answer

    def check_win(self):
        return len(self._card.numbers_on_card) == len(self._card.covered_numbers)

    @property
    def card(self):
        return self._card

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def answer(self):
        return self._answer
