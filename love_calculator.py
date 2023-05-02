name = input("Enter your name:")
name2 = input("Enter your lover name: ")

name = (name + name2).lower()

value = "true"
value2 = "love"


def love_calculator(name, value, value2):
    num1 = 0
    num2 = 0

    for i in value:
        num1 += name.count(i)
    
    for i in value2:
        num2 += name.count(i)
        
    result = int(str(num1) + str(num2))
    
    return result

love_score = love_calculator(name, value, value2)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score} , you go together like coke and mentos.")
    
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score} , you are alright together.")

else:
    print(f"Your score is {love_score}.")
    


    

