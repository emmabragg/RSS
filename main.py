import random
import user_bot

def game(player1score, player2score, player1shields, player2shields, matchstate1, matchstate2, bot_name):
    player1bullets = 0
    player2bullets = 0

    gamestate1 = []
    gamestate2 = []
    matchstate1.append([])
    matchstate2.append([])

    game_over = False

    while not game_over:
        # Gets moves from both players
        move1 = user_bot.make_move(gamestate1, matchstate1)
        move2 = bot_name(gamestate2, matchstate2)

        # Adds moves to matchstate and gamestate
        matchstate1[len(matchstate1) - 1].append([move1, move2])
        matchstate2[len(matchstate1) - 1].append([move2, move1])

        gamestate1.append([move1, move2])
        gamestate2.append([move2, move1])

        # Checks if either player has played too many shields
        if move1 == "S":
            player1shields += 1
            if player1shields >= 100:
                player2score += 1
                break

        if move2 == "S":
            player2shields += 1
            if player2shields >= 100:
                player1score += 1
                break

        # Counts each players bullets
        if move1 == "R":
            player1bullets += 1

        if move2 == "R":
            player2bullets += 1

        # Checks if a player attempts to fire with no bullets
        if move1 == "F" and player1bullets == 0:
            player2score += 1
            break

        if move2 == "F" and player2bullets == 0:
            player1score += 1
            break

        # Checks if a player kills the other player
        if move1 == "R" and move2 == "F":
            player2score += 1
            game_over = True

        if move2 == "R" and move1 == "F":
            player1score += 1
            game_over = True

        # Decreases a players bullets when they fire
        if move1 == "F":
            player1bullets -= 1

        if move2 == "F":
            player2bullets -= 1

    return (player1score, player2score, player1shields, player2shields, matchstate1, matchstate2)


def match(bot_name):
    # Vals hold the variables passed into each game
    # Vals[0] - player 1's score, Vals[1] - player 2's score
    # Vals[2] - player 1 shields used, Vals[3] - player 2 shields used
    # Vals[4] - matchstate1, Vals[5] - matchstate2

    vals = (0, 0, 0, 0, [], [])
    match_over = False

    while not match_over:
        # If someone hasn't one start a new game
        vals = game(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], bot_name)
        # If someone reaches 10 points they win
        if vals[0] >= 10 or vals[1] >= 10:
            match_over = True
            # Print the winner and the score
            print(vals[0], vals[1], end = '')
            if vals[0] >= 10:
                print(" - Player 1 wins")
            if vals[1] >= 10:
                print(" - Player 2 wins")


# Bot that always reloads
def reload_always_bot(gamestate, matchstate):
    return "R"


# Bot that chooses their move randomly between reload and fire
def random_RF_bot(gamestate, matchstate):
    rand = random.randrange(2)
    if rand == 0:
        return "R"
    elif rand == 1:
        return "F"


# Bot that chooses their move randomly between all 3 moves
def random_RFS_bot(gamestate, matchstate):
    rand = random.randrange(3)
    if rand == 0:
        return "R"
    elif rand == 1:
        return "S"
    else:
        return "F"


# Bot that reloads, then shoots, then reloads etc...
def reload_shoot_bot(gamestate, matchstate):
    if len(gamestate) == 0:
        return "R"
    if gamestate[len(gamestate) - 1][0] == "F":
        return "R"
    else:
        return "F"


# Bot that reloads, then shoots, then shields, then reloads etc...
def reload_shield_shoot_bot(gamestate, matchstate):
    if len(gamestate) == 0:
        return "R"
    if gamestate[len(gamestate) - 1][0] == "R":
        return "S"
    elif gamestate[len(gamestate) - 1][0] == "S":
        return "F"
    else:
        return "R"


# Bot that reloads then chooses their moves randomly between reload and fire
def reload_then_random_RF_bot(gamestate, matchstate):
    if len(gamestate) == 0:
        return "R"
    rand = random.randrange(2)
    if rand == 0:
        return "R"
    elif rand == 1:
        return "F"


# Bot that reloads then chooses their moves randomly between all 3 moves
def reload_then_random_RFS_bot(gamestate, matchstate):
    if len(gamestate) == 0:
        return "R"
    rand = random.randrange(3)
    if rand == 0:
        return "R"
    elif rand == 1:
        return "S"
    else:
        return "F"

# Bot that reloads if it doesn't have any bullets, otherwise does a random move
def track_own_bullets_RF_bot(gamestate, matchstate):
    # Bullet counter
    bullets = 0
    for i in range(len(gamestate)):
        if gamestate[i][0] == "R":
            bullets += 1
        elif gamestate[i][0] == "F":
            bullets -= 1

    # Decide which move to do
    if bullets == 0:
        move = "R"
    else:
        rand = random.randrange(2)
        if rand == 0:
            move = "R"
        elif rand == 1:
            move = "F"
    return move

# Bot that reloads if it doesn't have any bullets, otherwise does a random move
def track_own_bullets_RFS_bot(gamestate, matchstate):
    # Bullet counter
    bullets = 0
    for i in range(len(gamestate)):
        if gamestate[i][0] == "R":
            bullets += 1
        elif gamestate[i][0] == "F":
            bullets -= 1

    # Decide which move to do
    if bullets == 0:
        move = "R"
    else:
        rand = random.randrange(3)
        if rand == 0:
            move = "R"
        elif rand == 1:
            move = "S"
        else:
            move = "F"
    return move

# Bot that tracks both player's bullets and chooses a random 'useful' move
def track_all_bullets_RFS_bot(gamestate,matchstate):
    # Count the bullets of you and your opponent
    bullets = [0, 0]
    for i in range(len(gamestate)):
        for j in range(2):
            if gamestate[i][j] == "R":
                bullets[j] += 1
            elif gamestate[i][j] == "F":
                bullets[j] -= 1

    # Choose move based on bullets remaining.
    # If you have no bullets don't shoot.
    # If opponent has no bullets don't shield.
    if bullets[0] == 0:
        if bullets[1] == 0:
            move = "R"
        else:
            rand = random.randrange(2)
            if rand == 0:
                move = "R"
            elif rand == 1:
                move = "S"
    else:
        if bullets[1] == 0:
            rand = random.randrange(2)
            if rand == 0:
                move = "R"
            elif rand == 1:
                move = "F"
        else:
            rand = random.randrange(3)
            if rand == 0:
                move = "R"
            elif rand == 1:
                move = "S"
            elif rand == 2:
                move = "F"
    return move

print("")
print("Playing: RELOAD ALWAYS BOT")
match(reload_always_bot)
print("")
print("Playing: RANDOM RF BOT")
match(random_RF_bot)
print("")
print("Playing: RANDOM RFS BOT")
match(random_RFS_bot)
print("")
print("Playing: RELOAD SHOOT BOT")
match(reload_shoot_bot)
print("")
print("Playing: RELOAD SHIELD SHOOT BOT")
match(reload_shield_shoot_bot)
print("")
print("Playing: RELOAD THEN RANDOM RF BOT")
match(reload_then_random_RF_bot)
print("")
print("Playing: RELOAD THEN RANDOM RFS BOT")
match(reload_then_random_RFS_bot)
print("")
print("Playing: SMART RANDOM RF BOT")
match(track_own_bullets_RF_bot)
print("")
print("Playing: SMART RANDOM RFS BOT")
match(track_own_bullets_RFS_bot)
print("")
print("Playing: SMARTER RANDOM RFS BOT")
match(track_all_bullets_RFS_bot)
print("")