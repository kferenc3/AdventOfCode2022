#Part I:
#mapping: {'X' 'A': 1, 'B' 'Y': 2, 'C' 'Z': 3}
win =  [[3, 1], [1, 2], [2, 3]] #6
draw = [[1, 1], [2, 2], [3, 3]] #3
loss = [[2, 1], [3, 2], [1, 3]] #0

strategy = [[int(x),int(y)] for x,y in [i.replace('\n','').replace('A','1').replace('B','2').replace('C','3').replace('X','1').replace('Y','2').replace('Z','3').split(' ') for i in open('day_2_test.data')]]
points = 0

for game in strategy:
    points += game[1]
    if game in win:
        points += 6
    elif game in draw:
        points += 3

#Part I answer:
print('Part I points: ' + str(points))