# แก้ #1
delivery = int(input("ระยะทาง :"))
if delivery <= 5:
    print("-")
elif delivery <= 50:
    print("price = 10 baht")
elif delivery <= 100:
    print("price = 15 baht")
elif delivery <= 300:
    print("price = 25 baht")
elif delivery <= 500:
    print("price = 35 baht")
else:
    print("price 45 baht")

print("ระยะทาง :", delivery)