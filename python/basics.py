# basic commands in python

# basic hello world
print("hello world")
print('hello world 2')

for i in range(5):
    print("hello world few times")

print("""this hello world
        has multiple
        lines""")

# data types
my_str = "my string"
print(type(my_str))
my_int = 1
print(type(my_int))
my_float = 0.1
print(type(my_float))
my_bool = True
print(type(my_bool))
my_none_type = None
print(type(my_none_type))

# increase/decrease
num1 = 1
num1 += 1
print("num1 => " + str(num1))
num1 -= 2
print("num1 => " + str(num1))


# arithmetic operations
print("2 ** 3 => " + str(2 ** 3))
print("4 % 2 => " + str(4 % 2))
print("3 // 2 => " + str(3 // 2))
print("3 / 2 => " + str(3 / 2))
print("3 * 3 => " + str(3 * 3))
print("3 - 1 => " + str(3 - 1))
print("3 + 3 => " + str(3 + 3))


# comparison operators
print("1 > 2 => " + str(1 > 2))
print("1 < 2 => " + str(1 < 2))
print("1 >= 2 => " + str(1 >= 2))
print("1 <= 2 => " + str(1 <= 2))
print("1 == 2 => " + str(1 == 2))
print("1 != 2 => " + str(1 != 2))
print("not 1 == 1 => " + str(not 1 == 1))

# logical operators
print("1 < 2 and 1 != 0 => " + str(1 < 2 and 1 != 0))
print("1 > 2 or 1 != 0 => " + str(1 > 2 or 1 > 0))


# conditional statements
if 1 > 0:
    print("one is greater than zero")

if 1 > 2:
    print("one is greater")
else:
    print("one is less than two")

my_if_var = 3
if my_if_var == 1:
    print(1)
elif my_if_var == 2:
    print(2)
else:
    print("another number")


# functions
def print_function():
    print("Hellooooo")


print_function()


def print_function_with_param(my_value):
    print(my_value)


print_function_with_param("Another hello")


def add_two_numbers(n1, n2):
    return n1 + n2


print(add_two_numbers(2, 3))


def do_nothing():
    pass


x = 1
print("x => " + str(x))


def update_global_x(n1):
    global x
    x = n1


update_global_x(3)
print("x => " + str(x))


# built-in functions
print(len("samuel"))
# str, int, float, len, type, input, print, etc
name = input("what's your name? ")
print(name)


# exception handling
number1 = input("enter a number: ")
number2 = input("enter another number: ")
try:
    print(int(number1) / int(number2))
except ZeroDivisionError:
    print("second number cannot be zero")


# docstrings
def add(x, y):
    """
    Returns x + y
    :param x: int to be added
    :param y: int to be added
    :return: int sum of x and y
    """
    return x + y


print(str(add(5, 6)))


# containers

# list - mutable
empty_list = []
my_list = list()
my_list.append('car')
my_list.append(1)
my_list.append(True)
print(my_list)
my_list.pop()
print(my_list)

my_list2 = ['car', 'bike']
print(my_list2[1])
print("boat is in the list: " + str("boat" in my_list2))
print("boat is NOT in the list: " + str("boat" not in my_list2))
print("size of my_list2 is: " + str(len(my_list2)))

my_list3 = ["pizza", "pasta", "rice", "steak"]
print(my_list3[2:3])  # with slice, the end index is not included

my_list4 = ["coke", "sprite"]
print(my_list4)
my_list4.pop(0)
print(my_list4)
my_list4.insert(0, "coke")
print(my_list4)
my_list4 += ["cheeseburger", "cake"]
print(my_list4)
print(my_list4[-1])  # last item
print(my_list4[len(my_list4) - 1])  # last item

print(my_list4[1:])
print(my_list4[:1])

# methods in lists
my_list5 = ["apple", "banana", "cherry", "grape"]
print(my_list5)
my_list5.append("peach")
print(my_list5)
print("banana appears " + str(my_list5.count("banana")) + " time(s)")
my_list5.extend(["pear", "kiwi"])
print(my_list5)
print("pear is in index " + str(my_list5.index("pear")))
my_list5.insert(0, "lime")
print(my_list5)
my_list5.pop(5)
print(my_list5)
my_list5.remove("lime")
print(my_list5)
my_list5.reverse()
print(my_list5)
my_list5.sort()
print(my_list5)

# tuple - immutable
empty_tuple = ()
my_tuple = tuple("house")
my_tuple2 = ("car", "bike", "boat")
my_tuple3 = ("house",)  # tuple with only 1 item needs comma at the end
print(my_tuple2)
print(my_tuple2[1])
my_tuple_phone = ("61", "490953972")
print(my_tuple_phone)
country_code, mobile_number = my_tuple_phone
print("country code: " + country_code)
print("mobile: " + mobile_number)


# dictionary
empty_dictionary = {}
my_dictionary_empty = dict()
my_dictionary = {"Andre": 37, "Olga": 32, "Sam": 1}
print(my_dictionary)
del my_dictionary["Sam"]
print(my_dictionary)
my_dictionary.pop("Olga")
print(my_dictionary)
print(my_dictionary["Andre"])
my_dict = {"Andre": ["car", "bike"], "Olga": ["car"]}
print(my_dict)
print(my_dict["Andre"][1])
print("bike" in my_dict["Olga"])
print("car" and "bike" in my_dict["Andre"])


# strings
my_string = "hello world"
print(my_string.upper())
print(my_string.capitalize())
print(my_string.title())
print("andre"[::-1])  # reverse
print("andre"[::-2])

my_string2 = "ANDRE AND OLGA"
print(my_string2.lower())

string_multiple_lines = """Line1
Line 2
Line3"""
print(string_multiple_lines)

my_name = "ANDRE"
print(my_name[0])
print(my_name[-1])
my_year = 1982

print("I was born in {}".format(my_year))

names = "Andre,Olga".split(" ")
print(names)
print("+".join(my_name))
letters = "A,B,C,D"
print(letters.replace(",", ":"))
print(letters.index("B"))
print("E" in letters)
print("C" in letters)
print("Sam is my\nDOG")
print("*" * 30)


def my_func(param1, *other_params):
    for item in other_params:
        print(item)


my_func("param1", 1, 2, 3, 4, 5)


def my_func2(param1, **other_params):
    for key, value in other_params.items():
        print("key: {} and value: {}".format(key, value))


my_func2("bla", Name="Andre", Age=37)



