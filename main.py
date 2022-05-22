
import random
from art import logo
from replit import clear
def deal_cards():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  card=random.choice(cards)
  return card

def compare(user,computer):
  if user==0 and computer>0:
    print('User wins with blackjack')
  elif computer==0 and user>0:
    print('Computer wins with a blackjack')
  elif user>21:
    print('SCORE exceeds 21 You Lose')
  elif computer>21:
    print('User Wins')
  elif computer==user:
    print("it is a tie")
  else:
    if computer>user:
      print('computer wins')
    else:
      print('user wins')
                        
def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if sum(cards)>21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

  
def play():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over=False
  
  for i in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
  
  user_score= calculate_score(user_cards)
  computer_score= calculate_score(computer_cards)
    
  print(f'your cards are {user_cards} and the score is {user_score}')
  print(f'first card of computer is {computer_cards[0]} ')
  
  if user_score==0 or computer_score==0 or user_score>21:
    is_game_over=True
  
  
  while not is_game_over:
    choice= input('type y to take a new card from the deck ').lower()
      
    if choice=='y':
      user_cards.append(deal_cards())
      user_score=calculate_score(user_cards)
      print(f'your cards are {user_cards} and score is {user_score}')
      if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
      else:
        is_game_over=False
    else:
      is_game_over=True
  
  
  while is_game_over and computer_score!=0:
    if computer_score<17:
      computer_cards.append(deal_cards())
      computer_score=calculate_score(computer_cards)
    else:
      is_game_over=False
      print(f'computer cards are {computer_cards} and score is {computer_score}')
      compare(user_score,computer_score)
  
while input('to restart the game enter yes ').lower()=='yes':
  clear()
  play()
