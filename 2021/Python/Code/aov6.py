data = {}

with open("day 6.txt") as file:
    array = [int(x) for x in file.readline().split(',')]
    for value in range(max(9, max(array))):
        data[value] = 0
    for element in array:
        data[element] += 1

for days in range (256):
    zeroes = data[0]
    data[0] = 0
    for index in range(1, len(data)):
        data[index-1] += data[index]
        data[index] = 0
    data[6] += zeroes
    data[8] += zeroes

solution = 0
for key in data:
    solution += data[key]

print("P2 Sol:", solution)