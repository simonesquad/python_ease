print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

text = "Tim IS Great!"
print(text.lower())

if playing.upper() != "yes":
    quit() 

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
    score = score + 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does PSU stand for?")
if answer.lower() == "power supply":
    print('Correct!')
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
