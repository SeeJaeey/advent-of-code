from collections import defaultdict

input = """Player 1 starting position: 10
Player 2 starting position: 8"""

example = """Player 1 starting position: 4
Player 2 starting position: 8"""

lines = input.splitlines()

player1_start = int(lines[0][len(lines[0]) - 1])
player2_start = int(lines[1][len(lines[1]) - 1])

def part1(player1_start, player2_start):
    dice = [1, 2, 3]

    turn = 0
    rolls = 0

    player1_score = 0
    player2_score = 0

    while(player1_score < 1000 and player2_score < 1000):
        if turn:
            print(f"Player 2 rolls {dice[0]} + {dice[1]} + {dice[2]} and moves to space {player2_start + sum(dice) if player2_start + sum(dice) == 10 else (player2_start + sum(dice)) % 10}")
            player2_start += sum(dice)
            if player2_start % 10 != 0:
                player2_start = player2_start % 10
            else:
                player2_start = 10

            player2_score += player2_start

        else:
            print(f"Player 1 rolls {dice[0]} + {dice[1]} + {dice[2]} and moves to space {player1_start + sum(dice) if player1_start + sum(dice) == 10 else (player1_start + sum(dice)) % 10}")
            player1_start += sum(dice)
            if player1_start % 10 != 0:
                player1_start = player1_start % 10
            else:
                player1_start = 10

            player1_score += player1_start
        
        dice = [(dice[0] + 3) % 100, (dice[1] + 3) % 100, (dice[2] + 3) % 100]
        if dice[0] == 0:
            dice[0] = 100
        if dice[1] == 0:
            dice[1] = 100
        if dice[2] == 0:
            dice[2] = 100

        turn = 1 - turn
        rolls += 3

    print(rolls, player1_score)

    if player2_score < 1000:
        print(rolls * player2_score)
    else:
        print(rolls * player1_score)

def create3_universes(multiverse, player1, player2, score1, score2, c, w, p):
    for (d, f) in [(6, 7), (5, 6), (7, 6), (4, 3), (8, 3), (3, 1), (9, 1)]:
        np = ((player1 + d - 1) % 10) + 1
        ns = score1 + np
        if ns < 21:
            multiverse[(player2, np, score2, ns)] += c * f
        else:
            w[p] += c * f

def part2(player1, player2):
    multiverse = defaultdict(int)
    multiverse[(player1, player2, 0, 0)] = 1
    wins = [0, 0]
    turn = 0

    while multiverse:
        temp = defaultdict(int)
        for (player1, player2, score1, score2) in multiverse:
            create3_universes(temp, player1, player2, score1, score2, multiverse[(player1, player2, score1, score2)], wins, turn)
        turn = 1 - turn
        multiverse = temp

    return max(wins)

part1(player1_start, player2_start)

w = part2(player1_start, player2_start)
print(w)