# --- IMPORTS ---
import turtle
import time
import random

# --- CONFIG ---
WIDTH, HEIGHT = 800, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'pink', 'brown', 'cyan', 'black']

# --- PLAYER SELECT ---
def get_number_of_racers():
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Please enter a number between 2 and 10.")
        else:
            print("Invalid input. Please enter a number between 2 and 10.")

# --- SCREEN SETUP ---
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')
    screen.bgcolor('#f0f0f0')
    
    # Draw finish line
    line_painter = turtle.Turtle()
    line_painter.speed(0)
    line_painter.penup()
    line_painter.goto(340, 220)
    line_painter.pendown()
    line_painter.pensize(5)
    line_painter.color('red')
    line_painter.goto(340, -220)
    line_painter.hideturtle()

# --- CREATE RACERS ---
def create_racers(number_of_racers):
    turtles = []
    spacing = 400 // (number_of_racers - 1) if number_of_racers > 1 else 400
    
    racer_colors = COLORS[:number_of_racers]
    random.shuffle(racer_colors)

    for i, color in enumerate(racer_colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.penup()
        
        # Start positions
        start_x = -350
        start_y = -200 + (i * spacing)
        racer.goto(start_x, start_y)
        turtles.append(racer)
        
    return turtles

# --- GAME LOOP ---
def start_race(turtles):
    race_on = True
    while race_on:
        for racer in turtles:
            # Move random distance
            distance = random.randint(1, 10)
            racer.forward(distance)
            
            # Check for winner
            if racer.xcor() >= 340:
                race_on = False
                return racer.pencolor()

# --- SCOREBOARD ---
def display_scoreboard(winner_color):
    score_turtle = turtle.Turtle()
    score_turtle.speed(0)
    score_turtle.penup()
    score_turtle.goto(0, 0)
    score_turtle.hideturtle()
    score_turtle.color('black')
    
    # Text on screen
    score_turtle.write(
        f"🏆 THE WINNER IS: {winner_color.upper()}! 🏆", 
        align="center", 
        font=("Arial", 24, "bold")
    )

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    num_racers = get_number_of_racers()
    init_turtle()
    all_turtles = create_racers(num_racers)
    
    # Countdown
    print("Ready...")
    time.sleep(1)
    print("Set...")
    time.sleep(1)
    print("GO! 🏁")
    
    # Run race
    winner = start_race(all_turtles)
    
    # Show results
    display_scoreboard(winner)
    print(f"\nThe {winner} turtle won the race!")
    
    # Close window
    time.sleep(5)
