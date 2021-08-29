import random
from loto_classes import barrel, config


class Sack:
    def __init__(self):
        self._barrels = [barrel.Barrel(i + config.MIN_BARREL_NUMBER) for i in range(config.BARRELS_IN_SACK)]
        self._shake()

    def __repr__(self):
        return f"{self._barrels}"

    def __len__(self):
        return len(self._barrels)

    def _shake(self):
        """Impure: side effects and not deterministic"""
        random.shuffle(self._barrels)

    def pull_barrel(self):
        """Impure: side effects and not deterministic"""
        pulled = random.choice(self._barrels)
        self._barrels.remove(pulled)
        return pulled
