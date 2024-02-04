""" price = 25
while price >= 0:
    print(price)
    price -= 0.70

number = 0
while number < 20:
    if number%2 == 0:
        print(number)
    number += 1 """

# for num in range(100):
#     print(num)

people = ["Bryan", "Tammy", "Craig"]
for idx in range(len(people)):
    print(f'{people[idx]} is awesome!')


add_them = [1, 5, 7, 8]

for index in range(len(add_them)-1):
    print(add_them[index] + add_them[index + 1])