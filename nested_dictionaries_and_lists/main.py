# 1-1.
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)
print("\n")
# 1-2.

students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
students[0]["last_name"] = "Bryant"
print(students)
print("\n")

# 1-3.
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
print("\n")

# 1-4.
z = [{"x": 10, "y": 20}]
z[0]["y"] = 30
print(z)
print("\n")


# 2
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]


def interate_dictionary(some_list):
    for each_key in some_list:
        print(f"first_name - {each_key["first_name"]}, last_name - {each_key["last_name"]}")
    return ""

z = interate_dictionary(students)
print(z)
print("\n")

# 3
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]


def iterate_dictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])
    return ""


z = iterate_dictionary2("first_name", students)
print(z)
print("\n")

# 4.
dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": [
        "Michael",
        "Amy",
        "Eduardo",
        "Josh",
        "Graham",
        "Patrick",
        "Minh",
        "Devon",
    ],
}


def get_info(some_dict):
    print(f"{len(dojo['locations'])} LOCATIONS")
    for value in some_dict["locations"]:
        print(value)
    print("\n")

    print(f"{len(dojo['instructors'])} INSTRUCTORS")
    for value in some_dict["instructors"]:
        print(value)


y = get_info(dojo)
