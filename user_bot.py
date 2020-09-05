''' Write a bot to return one of three moves for each turn, either:
    reload - denoted 'R'
    shield - denoted 'S'
    fire - denotes 'F'

    you are provided both gamestate and matchstate

    gamestate is a 2D array containing all the past moves in the current game

    e.g. [['R', 'R'], ['S', 'F'], ['F', 'R']] for the move set

    player 1: R     player 2: R
    player 1: S     player 2: F
    player 1: F     player 2: R

    matchstate is a 3D array containing all of the past moves in the whole match

    e.g. [[['R', 'R'], ['F', 'R']], [['R', 'R'], ['S', 'S'], ['F', 'R']], [['R', 'R'], ['R', 'F']]]

    this would represent the move set

    game 1
    player 1: R     player 2: R
    player 1: F     player 2: R

    game 2
    player 1: R     player 2: R
    player 1: S     player 2: S
    player 1: F     player 2: R

    game 3
    player 1: R     player 2: R
    player 1: R     player 2: F

    Please note you will always be player 1

    REMEMBER: If you attempt to shield more than 100 times in a match, or you attempt to fire
    when you do not have enough bullets you will automatically lose that game

    See below a sample bot which would reload every time, edit the contents of the
    make_move function to get it to return as you wish

    Running the code will automatically play you against several basic sample bots       '''


def make_move(gamestate,matchstate):
    return "R"
