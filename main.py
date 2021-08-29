from loto_classes import Game, user_input

if __name__ == '__main__':
    new_game = True
    while new_game:
        players = user_input.ask_about_players()
        game = Game(players)
        game_result = game.play()
        new_game = user_input.ask_new_game()
