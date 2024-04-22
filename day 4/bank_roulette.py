names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
name =len(names)
bill = random.randint(0,name-1)

a = names[bill]

print(f"{a} is going to buy the meal today!")
