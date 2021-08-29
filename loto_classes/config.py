# GAME PARAMETERS
BARRELS_IN_SACK = 90
MIN_BARREL_NUMBER = 1
CARD_ROWS = 9
CARD_COLUMNS = 3
NUMBERS_ON_ROW = 5

# CARD APPEARANCE
SYMBOL_FOR_CELL_X = 4
TP_DELIMITER = '-'
LR_DELIMITER = '|'

# PLAYERS NUMBER
MIN_NUM_PLAYERS = 2
MAX_NUM_PLAYERS = 8

# GAME INNER PARAMETERS
HUMAN_TYPE_ID = 1
COMPUTER_TYPE_ID = 2
PLAYER_TYPES = {HUMAN_TYPE_ID: ['ч', 'h'], COMPUTER_TYPE_ID: ['к', 'c']}
ANSWER_TYPES = {False: ['н', 'n'], True: ['д', 'y']}

# DIALOGS
ASK_NUM_PLAYERS = f"Сколько игроков будет? ({MIN_NUM_PLAYERS}-{MAX_NUM_PLAYERS})"
ASK_PLAYER_TYPE = "Тип игрока #{0} (человек/компьютер)? " \
                  + f"({PLAYER_TYPES.get(HUMAN_TYPE_ID)[0]}/{PLAYER_TYPES.get(COMPUTER_TYPE_ID)[0]})"
ASK_PLAYER_NAME = "Как зовут игрока #{0}?"
BAD_INPUT = "Что-то не то ввели. Попробуйте снова."
CARD_NAME = "Карточка игрока {0}:"
COMP_NAME = "Компьютер #{0}"
HUMAN_NAME = "Человек #{0}"
NEXT_ROUND = "Раунд #{0}"
NEXT_BARREL = "Бочонок {0}"
IN_SACK = "Бочонков осталось в мешке: {0}"
ACT_PLAYER = "Твой ход, {0}. Ставим бочонок {1}? " \
             + f"({ANSWER_TYPES.get(True)[0]}/{ANSWER_TYPES.get(False)[0]})"
WRONG_ACT_TRUE = "Такого номера нет на твоей карте, {0}"
WRONG_ACT_FALSE = "Такой номер был на твоей карте, {0}"
LOSER = "{0} выбывает из игры"
WINNER = "Победитель - {0}!"
END_GAME = "Конец игры на раунде {0}"
ASK_NEW_GAME = f"Начать новую игру? ({ANSWER_TYPES.get(True)[0]}/{ANSWER_TYPES.get(False)[0]})"
