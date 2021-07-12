import pickle

t1 = [1, 2, 3]
s = pickle.dumps(t1)

t2 = pickle.loads(s)

print(t2)

FILENAME = "user.dat"
 
name = "Tom"
age = 19
 
with open(FILENAME, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
 
with open(FILENAME, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Имя:", name, "\tВозраст:", age)

DB = "users.dat"
 
users = [
    ["Tom", 28, True],
    ["Alice", 23, False],
    ["Bob", 34, False]
]
 
with open(DB, "wb") as file:
    pickle.dump(users, file)
 
 
with open(DB, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Имя:", user[0], "\tВозраст:", user[1], "\tЖенат(замужем):", user[2])
