numbers = [3,2,4,1]

print(numbers)
input('Press any key to continue.\n')

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]


print(numbers)



