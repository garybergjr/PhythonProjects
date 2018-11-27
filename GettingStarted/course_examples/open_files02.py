f = open("scores.txt", "r")

participants = {}

for line in f:
    print(line.strip().split(","))

f.close()
