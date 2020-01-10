import csv
import json

my_file = open("hello.txt", "w")
my_file.write("Hello Andre")
my_file.close()

with open("hello2.txt", "w") as my_file2:
    my_file2.write("My name is Andre")

with open("hello2.txt", "a") as my_file:
    my_file.write("\nand my name is Olga")

with open("hello2.txt", "r") as my_file: # "r" is the default
    for line in my_file:
        print("*" * 30)
        print(line)

my_list = list()
with open("hello.txt", "r") as my_file:
    for line in my_file:
        my_list.append(line)

print("*" * 30)
print(my_list)

my_list2 = list()
with open("hello.txt", "r") as f:
    my_list2 = f.readlines()

print("*" * 30)
print(my_list2)

my_list3 = [line.rstrip('\n') for line in open("hello.txt", "r")]
print("*" * 30)
print(my_list3)


with open("my_file.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    spamwriter.writerow(["one", "two", "three"])
    spamwriter.writerow(["four", "five", "six"])


with open("my_file.csv", "r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    for row in spamreader:
        print(",".join(row))


my_dict = {
    "Name": "Andre",
    "Age": 37,
    "Email": "andre.fernandes@myob.com"
}
with open("my_json.json", "w") as f:
    json.dump(my_dict, f)

with open("my_json.json", "r") as f:
    x = json.load(f)
    print(json.dumps(x, indent=4))  # , sort_keys=True))

