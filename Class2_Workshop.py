delivery = input("ระยะทาง :")
if int(delivery) <= int(5):
    print("-")
elif int(delivery) <= int(50):
    print("price = 10 baht")
elif int(delivery) <= int(100):
    print("price = 15 baht")
elif int(delivery) <= int(300):
    print("price = 25 baht")
elif int(delivery) <= int(500):
    print("price = 35 baht")
else:
    print("price 45 baht")

print("ระยะทาง :", delivery)