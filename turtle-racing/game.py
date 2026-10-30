
# Function to start the game while true & player amount select
def get_number_of_racers():
    racers = 0
    while true:
    # running the game
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Please enter a number between 2 and 10.")
        else:
            print("Invalid input. Please enter a number between 2 and 10, racer amount.")
            # Maximum 10 racers minimum 2 racers

# Turtle setup function
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

# create a turtle for each racer
racer = turtle.Turtle()
racer.forward(100)
racer.left(90)
racer.forward(100)
racer.right(90)
racer.backward(100)
timer.sleep(5)


