# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split('\n'))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
turns = 0

def simulate_war(player1_cards, player2_cards, turn_limit):
  global turns
  while len(player1_cards) > 0 and len(player2_cards) > 0 and turns < turn_limit:
    player1_card = player1_cards.pop(0)
    player2_card = player2_cards.pop(0)

    if values.index(player1_card) > values.index(player2_card):
    #   player1_cards.append(player1_card)
      player1_cards.append(player2_card)
    elif values.index(player2_card) > values.index(player1_card):
    #   player2_cards.append(player2_card)
      player2_cards.append(player1_card)
    else:
    #   # The cards are tied. Return them to the bottom of the pile and compare
    #   # the next cards.
      player1_cards.append(player1_card)
    #   player1_cards.append(player2_card)
      player2_cards.append(player2_card)
    #   player2_cards.append(player1_card)
    
        # Increment the turn count.
    turns += 1

  # If the turn limit is reached, the game ends in a draw.
    if turns == turn_limit:
        return "draw"


  if len(player1_cards) == 0:
    return "player 2"
  elif len(player2_cards) == 0:
    return "player 1"
  else:
    return "draw"


num_games = int(get_number())

for i in range(num_games):
    player1_cards = get_word().split()
    player2_cards = get_word().split()
    turn_limit = 100000

    winning_player = simulate_war(player1_cards, player2_cards, turn_limit)
    
    print(winning_player)
