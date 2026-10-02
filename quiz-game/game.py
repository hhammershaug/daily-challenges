def play():
    print("okey! We play")
    # Declare the score variable starting at 0
    score = 0
    questionAmount = 2

    # --- Question 1 ---
    answer1 = input("What does CPU stand for? ").lower()

    if answer1 == "central processing unit":
        print("Correct!")
        score += 1  # Add 1 point
    else:
        print("False!")

    # --- Question 2 ---
    answer2 = input("What does RAM stand for? ").lower()

    if answer2 == "random access memory":
        print("Correct!")
        score += 1  # Add another point
    else:
        print("False!")

    # --- Final Score ---
    # Using an f-string to easily insert the variables into the text
    print(f"score = {score}/{questionAmount}")


# Her starter selve programmet
print("Welcome to my computer quiz!")

playing = input("Do you wanna play quiz-game? ").lower()

if playing == "yes":
    play()
else:
    quit()
