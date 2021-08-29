import random
from loto_classes import config


class Card:
    def __init__(self):
        self._card_list = self._generate_card()
        self._numbers_on_card = self._get_numbers_on_card()
        self._covered_numbers = list()

    def __repr__(self):
        return f"{self._card_list}"

    def __str__(self):
        top = (config.TP_DELIMITER + config.TP_DELIMITER * config.SYMBOL_FOR_CELL_X) * config.CARD_ROWS + config.TP_DELIMITER + '\n'
        image = ''
        for column in range(config.CARD_COLUMNS):
            image += top
            for row in range(config.CARD_ROWS):
                if row + 1 in self._card_list[column][0]:
                    index = self._card_list[column][0].index(row + 1)
                    number = self._get_cell_pic(self._card_list[column][1][index])
                    image += config.LR_DELIMITER + number.rjust(config.SYMBOL_FOR_CELL_X, ' ')
                else:
                    image += config.LR_DELIMITER + ''.rjust(config.SYMBOL_FOR_CELL_X, ' ')
            image += config.LR_DELIMITER + '\n'
        image += top
        return f"{image}"

    def _get_cell_pic(self, number):
        if number in self._covered_numbers:
            return f"({number})"
        return f"{number}"

    @staticmethod
    def _generate_card():
        """Impure: no side effects, but not deterministic"""
        card = list()
        positions_all = [n + 1 for n in range(config.CARD_ROWS)]
        numbers_all = [k + config.MIN_BARREL_NUMBER for k in range(config.BARRELS_IN_SACK)]
        random.shuffle(numbers_all)
        pointer = 0
        for i in range(config.CARD_COLUMNS):
            row = list()
            random.shuffle(positions_all)
            positions = positions_all[0:config.NUMBERS_ON_ROW]
            positions.sort()
            row.append(positions)
            numbers = numbers_all[pointer:pointer + config.NUMBERS_ON_ROW]
            numbers.sort()
            row.append(numbers)
            pointer += config.NUMBERS_ON_ROW
            card.append(row)
        return card

    def _get_numbers_on_card(self):
        numbers = list()
        for i in range(config.CARD_COLUMNS):
            numbers.extend(self._card_list[i][1])
        return numbers

    def cover_card_cell(self, barrel):
        """Impure: deterministic but with side effects"""
        if barrel.number in self._numbers_on_card:
            self._covered_numbers.append(barrel.number)

    @property
    def numbers_on_card(self):
        return self._numbers_on_card

    @property
    def covered_numbers(self):
        return self._covered_numbers
