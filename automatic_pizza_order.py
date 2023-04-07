print("Welcome to the Pizza Deliveries!")

while True:
    size = input("What size pizza do you want? S, M, L  :").lower()
    if size == 's' or size == 'm' or size == 'l':
        break
    else:
        print("please enter valid input and try again ")
        

while True:   
    add_peperoni = input("Do you want to add peperoni ? Y or N  :").lower()
    if add_peperoni == 'y' or add_peperoni == 'n':
        break
    else:
        print("please enter valid input and try again ")

while True:
    extra_cheese = input("Do you want to add extra cheese ? Y or N :").lower()
    
    if extra_cheese == 'y' or extra_cheese == 'n' :
        break
    else:
        print("please enter valid input and try again ")
    


small_cost = 15
medium_cost = 20
large_cost = 25

peperoni_small_cost = 2
peperoni_medium_and_large_cost = 3
extra_cheese_cost = 1

bill = 0


if size == 's':
    bill += small_cost
    if add_peperoni == 'y':
        bill += peperoni_small_cost
    if extra_cheese == 'y':
        bill += extra_cheese_cost
elif size == 'm':
    bill += medium_cost
    if add_peperoni == 'y':
        bill += peperoni_medium_and_large_cost
    if extra_cheese == 'y':
        bill += extra_cheese_cost

elif size == 'l':
    bill += large_cost
    if add_peperoni == 'y':
        bill += peperoni_medium_and_large_cost
    if extra_cheese == 'y':
        bill += extra_cheese_cost


print(f"Your bill is $ {bill}")
        
        
    
    
    




