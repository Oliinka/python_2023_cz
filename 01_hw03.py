name = str(input("What is your first name? "))
surname = input("What is your surname? ")
full_name = print(name + " " + surname)

print(full_name)
print(name.title()+ " " + surname.title())
print(name.upper()+ " " + surname.upper())

fullname = [name, surname]
print(fullname)

# printing the list using loop
for x in range(len(a)):
    print a[x]