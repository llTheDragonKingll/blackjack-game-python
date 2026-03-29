import random
import os
def clear_screen():
    os.system('cls')
def deal_cards():
    cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
    return random.choice(cards)
clear_screen()
while True:
    print(''' 
       _________                                                             
      |A        |                       _     _            _    _            _                                             
      | ♠       |                      | |   | |          | |  (_)          | |   
      |   ♠     |                      | |__ | | __ _  ___| | ___  __ _  ___| | __                                           
      |   ♠     | _________            | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /                                            
      |      ♠  ||10       |           | |_) | | (_| | (__|   <| | (_| | (__|   <        
      |        A||  ♥      |           |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\    
       ‾‾‾‾‾‾‾‾‾ |    ♥♥   |                                  _/ |        
                 |      ♥  |                                 |__/    
                 |       10|
                 |_________|
''')
    players_cards = []
    computers_cards_out = []
    computers_cards = []
    for n in range (2):
        players_cards.append(deal_cards())
        computers_cards.append(deal_cards())
    computers_cards_out.append(computers_cards[0])
    computers_cards_out.append("🃏")
    players_sum = sum(players_cards)
    computers_sum = sum(computers_cards)
    print(f"Your cards: {players_cards}       Computers cards: {computers_cards_out}")
    print(f"Your total: {players_sum}")
    while computers_sum <= 17:
        computers_cards.append(deal_cards())
        computers_sum = sum(computers_cards)
    hit_or_stands = True
    while hit_or_stands:
        if computers_sum > 21:
                hit_or_stands = False
                print(f"Your cards: {players_cards}       Computers cards: {computers_cards}")
                print(f"Your total: {players_sum}         Computers Sum: {computers_sum}")
                print("Computer Burts, You Win!!!")
        elif players_sum > 21:
                hit_or_stands = False
                print(f"Your cards: {players_cards}       Computers cards: {computers_cards}")
                print(f"Your total: {players_sum}         Computers Sum: {computers_sum}")
                print("You Burst, Computer Wins!!!")
        else:
            hit_or_stand = input("Hit or Stand? ").lower()
            if hit_or_stand == "hit":
                players_cards.append(deal_cards())
                players_sum = sum(players_cards)
                print(f"Your cards: {players_cards}       Computers cards: {computers_cards_out}")
                print(f"Your total: {players_sum}")
            else:
                hit_or_stands = False
                if players_sum > computers_sum:
                    print(f"Your cards: {players_cards}       Computers cards: {computers_cards}")
                    print(f"Your total: {players_sum}         Computers Sum: {computers_sum}")
                    print("You Win!!!")
                elif players_sum < computers_sum:
                    print(f"Your cards: {players_cards}       Computers cards: {computers_cards}")
                    print(f"Your total: {players_sum}         Computers Sum: {computers_sum}")
                    print("You Lose!!!")
                elif players_sum == computers_sum:
                    print(f"Your cards: {players_cards}       Computers cards: {computers_cards}")
                    print(f"Your total: {players_sum}         Computers Sum: {computers_sum}")
                    print("Its a Draw!!!")            
    new_game_input = input("Do you want to play again? ").lower()
    if new_game_input == "yes":
        clear_screen()
        continue
    else:
        break
