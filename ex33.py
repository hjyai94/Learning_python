i = 0
numbers = []

def f1(i):
    if i < 6:
        return 1
    else:
        return 0

while f1(i):
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
