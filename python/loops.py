# for
for i in range(5, 10):
    print(i)

for _ in range(1):
    print("ANDRE and OLGA")

for character in "ANDRE":
    print(character)

my_list = ["banana", "apple", "peach", "cherry"]
for item in my_list:
    print(item)

my_dict = {"Andre": 37, "Olga": 32}
for key in my_dict:
    print(key)

for value in my_dict.values():
    print("Age is: " + str(value))

for key in my_dict.keys():
    print("The name is: " + key)

for key, value in my_dict.items():
    print("Name is {} and age is {}".format(key, value))

# while
i = 0
while True:
    print(i)
    i += 1
    if i == 5:
        break

for i in range(5):
    if i == 2:
        continue

    print(i)
