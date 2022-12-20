with open('input.txt', 'r') as infile:
    strategy = infile.read().strip().split("\n")

standard = {'X': 1, 'Y': 2 , 'Z': 3,
            'A': 1, 'B': 2, 'C': 3}

score = 0
for line in strategy:
    opp, me = line.split()
    if standard[me] == standard[opp]:
        score += 3 + standard[me]
    elif standard[me] - standard[opp] == -2 or standard[me] - standard[opp] == 1:
        score += 6 + standard[me]
    else:
        score += standard[me]

print(score)

