# a = 5
# while a > 0:
#     print(a)
#     a -= 1
# while True:
#     usr_cmd = input("Enter your cmd: ")
#     if usr_cmd == "quit":
#         break
#     else:
#         print("You typed " + usr_cmd)


print('''Please pick one:
      rock
      scissors
      paper''')
while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("player a: "))
    player_b = str(input("player_b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another gam, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another gam, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw. Please continue.')
        print('')
