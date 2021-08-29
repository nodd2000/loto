from loto_classes import config


def correct_input_decorator(func):
    def correct_input_wrapper(*args):
        is_process_done = False
        result = None
        while not is_process_done:
            result = func(args)
            if result is not None:
                is_process_done = True
            else:
                print(config.BAD_INPUT)
        return result

    return correct_input_wrapper


def parse_players_num(user_input):
    try:
        if int(user_input) > config.MAX_NUM_PLAYERS or int(user_input) < config.MIN_NUM_PLAYERS:
            user_input = None
        else:
            user_input = int(user_input)
    except ValueError:
        user_input = None
    return user_input


def parse_player_type(user_input):
    user_input = user_input.lower()
    if user_input in config.PLAYER_TYPES.get(config.HUMAN_TYPE_ID):
        user_input = config.HUMAN_TYPE_ID
    elif user_input in config.PLAYER_TYPES.get(config.COMPUTER_TYPE_ID):
        user_input = config.COMPUTER_TYPE_ID
    else:
        user_input = None
    return user_input


def parse_player_act(user_input):
    user_input = user_input.lower()
    if user_input in config.ANSWER_TYPES.get(True):
        user_input = True
    elif user_input in config.ANSWER_TYPES.get(False):
        user_input = False
    else:
        user_input = None
    return user_input


def parse_new_game(user_input):
    user_input = user_input.lower()
    if user_input in config.ANSWER_TYPES.get(True):
        user_input = True
    elif user_input in config.ANSWER_TYPES.get(False):
        user_input = False
    else:
        user_input = None
    return user_input


def ask_player_name(num):
    print(config.ASK_PLAYER_NAME.format(num))
    return input()


@correct_input_decorator
def ask_num_players(num):
    if num is None:
        pass
    print(config.ASK_NUM_PLAYERS)
    user_input = parse_players_num(input())
    return user_input


@correct_input_decorator
def ask_player_type(num):
    print(config.ASK_PLAYER_TYPE.format(num[0]))
    user_input = parse_player_type(input())
    return user_input


@correct_input_decorator
def ask_player_act(name):
    user_input = parse_player_act(input())
    return user_input


@correct_input_decorator
def ask_new_game(emp):
    print(config.ASK_NEW_GAME)
    user_input = parse_new_game(input())
    return user_input


def ask_about_players():
    players_num = ask_num_players()
    players = list()
    for num in range(players_num):
        player_id = num + 1
        if ask_player_type(player_id) == config.HUMAN_TYPE_ID:
            player_name = ask_player_name(player_id)
            player_type = config.HUMAN_TYPE_ID
        else:
            player_name = config.COMP_NAME.format(player_id)
            player_type = config.COMPUTER_TYPE_ID
        players.append({"id": player_id, "name": player_name, "type": player_type})
    return players
