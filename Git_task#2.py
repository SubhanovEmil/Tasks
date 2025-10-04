# Problem: Write a Python program that takes a range of numbers (start, end)
#  and prints all prime numbers in that range.

# 8, 9, 10, 11, 12, 13, 14, 15, 17, 19

start = int(input())
end = int(input())
numbers = []
prime_numbers = []

for element in range(start,end + 1):
    numbers.append(element)

for number in numbers:
    counter = 0
    for i in range(1, number +1):
        if number % i == 0:
            counter += 1
    if counter == 2:
        prime_numbers.append(number)
print(*prime_numbers, sep="\n")


