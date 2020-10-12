import random


# Easy game of Rock,Paper,Scissors
variants_for_computer = ('Rock', 'Paper', 'Scissors')
point_player = 0
point_comp = 0




print('Welcome to the game Rock, Paper, Scissors!')
print('\n')


while point_player <= 10 and point_comp <= 10:
    player_answer_1 = str(input('Okay,here is your try, write R for Rock, S for Scissors and P for Paper').capitalize())
    if player_answer_1 == 'R':
        player_answer_1 = 'Rock'
    elif player_answer_1 == 'S':
        player_answer_1 = 'Scissors'
    elif player_answer_1 == 'P':
        player_answer_1 = 'Paper'
    else:
        print('Sorry, but you should write right letter for next time,bye')
    comp_answer_1 = variants_for_computer[random.randrange(len(variants_for_computer))]
    if point_comp == 10:
        print('Computer got 10 points and won this game')
        break
    elif point_player == 10:
        print('You go 10 points and won this game')
        break
    elif player_answer_1 == comp_answer_1:
        print('Wow it\'s a draw!')
        print('No one gets a point!')
    elif player_answer_1 == 'Scissors' and comp_answer_1 == 'Paper':
        print('Scissors beats Paper so you get 1 point')
        point_player += 1
        print(f'Your points are {point_player},and you enemy points {point_comp}')
    elif comp_answer_1 == 'Scissors' and player_answer_1 == 'Paper':
        print('Scissors beats Paper so your opponent gets 1 point')
        point_comp += 1
        print(f'Your points are {point_player},and you enemy points {point_comp}')
    elif player_answer_1 == 'Rock' and comp_answer_1 == 'Paper':
        print('Rock beats Paper so you get 1 point')
        point_player += 1
        print(f'Your points are {point_player},and you enemy points {point_comp}')
    elif player_answer_1 == 'Paper' and comp_answer_1 == 'Rock':
        print('Rock beats Paper so your opponnet gets 1 point')
        point_player += 1
        print(f'Your points are {point_player},and you enemy points {point_comp}')
    elif player_answer_1 == 'Scissors' and comp_answer_1 == 'Rock':
        print('Rock smashed scissors!')
        point_comp += 1
        print(f'Your points are {point_player},and you enemy points {point_comp}')
    elif player_answer_1 == 'Rock' and comp_answer_1 == 'Scissors':
        print('Rock smashed scissors!')
        point_player += 1
        print(f'Your points are {point_player},and you enemy points {point_comp}')
    else:
        print('Sorry but you wrote something wrong ')
        print("\n")
        print('Game ends for you,I\'m sorry!')
        break


