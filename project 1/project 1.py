# collect the data
print("hello we are here collect the some data ")
print("welcome to this side")


#collect the some information


name = input("Please enter your name here: ")
age = int(input("Please enter your age here: "))
height = float(input("Please enter your height here S: "))
fav_number = int(input("Please enter your favourite number here: "))

print("\nThank you for giving the information:\n")


#print variables details
print("name:", name, "Type:",type(name), "Memory Address:",id(name))
print("age:", age, "Type:",type(age), "Memory Address:",id(age))
print("height:", height, "Type:",type(height), "Memory Address:",id(height))
print("Favouroite number:", fav_number, "Type:",type(fav_number), "Memory Address:",id(fav_number))


#data in process
current_year = 2025
birth_year = current_year - age

print("\n your birth year is here based on approximent;",birth_year)

#summary
print("\nUSER SUMMARY")
print("Hello", name)
print("you are",age,"years old")
print("your height is ", height,)
print("your favourite number is",fav_number)
print("your approximent birth year is",birth_year)
print("-----------------------------")


#exit message
print("\nThank you for help the data collectoion")     



