name = "난현성"
age = 20
score = 95.5

print("Hello, Python!")

print("Name:", name, "Age:", age, "Score:", score)

print(f"My name is {name}, I am {age} years old, score: {score}")

print("My name is {}, I ame {} years old, score: {}".format(name, age, score))
print("My name si {0}, age {1}, score {2}".format(name, age, score))
print("Score with 2 decimals: {:.2f}".format(score))

print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))

print("This is line 1\nThis is line 2")

print("Hello", end=" ")
print("World!")

print("2025", "09", "23", sep="-")

data = {"name": name, "age": age, "score": score}
print ("Data:", data)

print(f"Next year age: {age + 1}")
print(f"Score (rounded): {round(score)}")

print(f"""
Student Info:
 - Name : {name}
 - Age  : {age}
 - Score: {score:.2f}
""")