print("welcome to Rollercoaster!")

height = float(input("What is your height in cm? : "))

height_limit = 120
adult = 18
adult_cost = 120
child_cost = 60



if height >= height_limit:
    print("You can ride the rollercoaster")
    age = int(input("what is your age ?: "))
    if age >= adult:
        print(f"you need to pay {adult_cost}")
    
    else:
        print(f"you need to pay {child_cost}")

else:
    print("sorry, you can't ride the rollercoaster")



