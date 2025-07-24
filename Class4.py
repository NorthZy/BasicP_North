# def tis(a, b):
#     return a + b

# print(tis(40, 50))

# x = 15124
# y = 94923


# def add(a,b):
#     print(a+b)
# add(x,y)

# def TellAge():
#     Age = input("Enter your age:")
#     print("I am ", Age, "years old")

# def Food():
#     food = input("Your favorite food :")
#     print("My favorite food is", food)

# def introduction(eiei):
#     print("My name is", eiei)
#     TellAge()
#     Food()



# introduction("North")


# วนกี่รอบ = (int(input("จำนวนรอบ :")))
# def Spam(xd):
#     for i in range(1,วนกี่รอบ + 1):
#         print(xd)

# Spam("eiei")

# a = 20
# b = 30
# def buoak(a, b):
#     return a + b

# result = buoak(a,b)

# print(result)

# list_1 = ["Hello", 58593, 3.14, "looool"]
# list_1[2] = 7
# list_1[3] = 44444
# list_1.append("hahahahaha")
# a = "นายบี"
# list_1.append(a)
# list_1.pop(2)
# list_1.pop()
# for i in list_1:
#     if i == 44444:u8
#         print("nice!")

# dict_a = {"hahahahaha":"lol", "sybau":"annoying"}
# # print(dict_a["sybau"])

# students = [
#     {"name": "Tom", "id": 11, "score" : 52},
#     {"name": "James", "id": 62, "score": 48},
#     {"name": "Eiei", "id": 14, "score": 99}
# ]

# for students in students:
#     print(students["name"])
#     print(students["id"])
#     print(students["score"])

students = [
    {"name": "Tom", "money": 1000},
    {"name": "Jerry", "money": 1000},
    {"name": "Tony Stonk", "money": 1000000},
    {"name": "Tony but not stonk", "money": 10}
]

def checkmoney(students):
    for students in students:
        if students["money"] > 500:
            print("omg so richh!!!(more than 500)")
    else:
        print("lol so poooor(less than 500)") 
    
checkmoney(students)