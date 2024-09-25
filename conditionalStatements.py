age = int(input("Enter your age:"))

if(age < 20 and age > 10):
    print("You are in your teenage")
elif(age > 20 and age < 30):
    print("You are an adult.")
elif(age > 30 and age < 50):
    print("You are a Man.")
elif(age > 50):
    print("You are an Old Man.")
else:
    print("You are a child.")