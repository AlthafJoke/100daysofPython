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

bill = 0


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
        bill += adult_cost
        
        if photography:
            bill +=  photography_charge
        
         
    if age >= 45 and age <= 55:
        bill = 0
        print("Everything is have free ride on us")
        
    else:
        bill += child_cost
        if photography:
           bill += photography_charge
        
        
      
else:
    print("sorry, you can't ride the rollercoaster")
    

print(f"You need to pay {bill}")



