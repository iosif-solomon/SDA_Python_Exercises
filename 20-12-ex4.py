
# ? Write a Python program to count the number of even and odd numbers from a series of numbers. 
# * Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# * Expected Output : 
# * Number of even numbers : 5
# * Number of odd numbers : 4

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# ! Varianta 1 - cu for loop 
evens = 0
odds = 0
for num in numbers:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

# ! Varianta 2 - cu list comprehension
evens = len([num for num in numbers if num % 2 == 0])
odds = len([num for num in numbers if num % 2 != 0])

print(f"Number of even numbers: {evens}")
print(f"Number of odd numbers: {odds}")



# ? Count how many times a number appears in a list
numbers2 = [1,1,2,2,2,4]

# ! * Rezolvare 1
numbers_count = {}
for num in numbers2:
    if numbers_count.get(num) is None:
        numbers_count[num] = 1
    else:
        numbers_count[num] += 1
for num, count in numbers_count.items():
    print(f"The number {num} appears {count} in our list")


# ! Rezolvare 2
numbers_count2 = {}
for num in numbers2:
    numbers_count2[num] = numbers2.count(num)
for num, count in numbers_count2.items():
    print(f"The number {num} appears {count} in our list")