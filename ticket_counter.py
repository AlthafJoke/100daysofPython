print("welcome to Rollercoaster!")
print("""
        Ticket price:
      -----------------
      Adult : $ 120
      minor : $ 60
      photography: $ 20
      ------------------
      """)

height = float(input("What is your height in cm? : "))

height_limit = 120
adult = 18
adult_cost = 120
child_cost = 60
photography_charge = 20



if height >= height_limit:
    print("You can ride the rollercoaster")
    age = int(input("what is your age ?: "))
    
    while True:
        photography = (input("Do you want photography? yes or no ? :")).lower()
        
        if photography == 'yes':
            photography = True
            break
        elif photography == 'no':
            photography = False
            break
        else:
            print("please provide valid input")
      
    
    if age >= adult:
        if photography:
            print(f"you need to pay {adult_cost + photography_charge}")
        else:
            print(f"you need to pay {adult_cost}")
        
    else:
        if photography:
            print(f"you need to pay {child_cost + photography_charge}")
        
        else:
            print(f"you need to pay {child_cost}")

else:
    print("sorry, you can't ride the rollercoaster")



