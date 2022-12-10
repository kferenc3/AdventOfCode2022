#Part II: X-Lose, Y-Draw, Z-Win
outcome = {1: 0, 2: 3, 3: 6}
beats = {1: 2, 2: 3, 3: 1}


strategy = [[int(x),int(y)] for x,y in [i.replace('\n','').replace('A','1').replace('B','2').replace('C','3').replace('X','1').replace('Y','2').replace('Z','3').split(' ') for i in open('day_2_test.data')]]
points = 0

for game in strategy:
    points += outcome[game[1]]
    if game[1] == 2:
        points += game[0]
    elif game[1] == 3:
        points += beats[game[0]]
    elif game[1] == 1:
        points += beats[beats[game[0]]]

print('Part II points: ' + str(points))

