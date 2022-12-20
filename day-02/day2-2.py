with open('input.txt', 'r') as infile:
    strategy = infile.read().strip().split("\n")

standard = {'X': -1, 'Y': 0 , 'Z': 1,
            'A': 0, 'B': 1, 'C': 2}

score = 0
order = [1,2,3]
for line in strategy:
    opp, me = line.split()
    score += (standard[me] + 1) * 3
    score += order[(standard[opp] + standard[me])%3]

print(score)

