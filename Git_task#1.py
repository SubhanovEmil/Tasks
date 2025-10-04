#**Problem**: Write a Python program that takes a list of dictionaries where each dictionary contains information about a person (`name`, `age`, and `city`). The program should:
# 1. Print the names of all people who are older than 25.
# 2. Sort the list by `age` in descending order and print the sorted list.

people = [
    {'name': 'John', 'age': 32, 'city': 'California'},
    {'name': 'Amy', 'age': 24, 'city': 'Oregon'},
    {'name': 'Geralt', 'age': 21, 'city': 'New Jersey'},
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 22, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
    ]

print("Names of people older than 25:")
for i in people:
    if i['age'] > 25:
        print(i['name'])
print()

sorted_people = sorted(people, key=lambda x: x['age'], reverse=True)
print("Sorted by age (descending):")
for i in sorted_people:
    print(i)























