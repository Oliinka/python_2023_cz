name = input("Pleas type your name: ")

age_min = 13
age_max = 105
age_type = 0
limit = 1
while age_type < limit:
    age = int(input(f"Dear {name} what is your age?: "))
    age_type += 1
    if age >= age_max:
        print("Pleas, print in your real age.")
    elif age <= age_min:
        print("Sorry, your age is not acceptable for this transaction.")
        break
else:
    print("""
   
    Welcome to our shop!
    Pleas, pick one of our performances.
    
    """)

