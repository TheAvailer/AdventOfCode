def NoOfIncreases(data):
    increases = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            increases +=1
    return increases


with open("day 1.txt") as file:
    answer = [int(x) for x in file.read().split()]

print("P1: ", NoOfIncreases(answer))

answer2 = []
for i in range(2, len(answer)):
    answer2.append(answer[i] + answer[i-1] + answer[i-2])

print("P2: ", NoOfIncreases(answer2))