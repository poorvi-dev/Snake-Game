# Importing necessary modules
import turtle  # For graphics and game setup
import time    # To control game speed
import random  # To generate random positions for food

# Initial delay for game speed
delay = 0.1

# Variables to track score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()  # Create game window
wn.title("Snake Game")  # Set window title
wn.bgcolor("black")  # Set background color
wn.setup(width=600, height=600)  # Set window dimensions
wn.tracer(0)  # Turn off automatic screen updates for smoother animations

# Snake head setup
head = turtle.Turtle()  # Create the snake's head
head.speed(0)  # Animation speed (0 means fastest)
head.shape("circle")  # Set the shape of the head
head.color("white")  # Set color of the head
head.penup()  # Disable drawing when the head moves
head.goto(0, 0)  # Start position of the head
head.direction = "stop"  # Initial movement direction is stopped

# Food setup
food = turtle.Turtle()  # Create the food object
food.speed(0)  # Animation speed
food.shape("square")  # Set the shape of the food
food.color("red")  # Set color of the food
food.penup()  # Disable drawing when the food moves
food.goto(0, 100)  # Initial position of the food

# List to store snake body segments
segments = []

# Pen setup for score display
pen = turtle.Turtle()  # Create a turtle object for displaying score
pen.speed(0)  # Animation speed
pen.shape("square")  # Set the shape of the pen (irrelevant as it is hidden)
pen.color("white")  # Set the pen color
pen.penup()  # Disable drawing
pen.hideturtle()  # Hide the pen
pen.goto(0, 260)  # Position the pen at the top of the screen
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))  # Initial score display

# Functions to change snake direction
def go_up():
    if head.direction != "down":  # Prevent reversing direction
        head.direction = "up"  # Set direction to up

def go_down():
    if head.direction != "up":  # Prevent reversing direction
        head.direction = "down"  # Set direction to down

def go_left():
    if head.direction != "right":  # Prevent reversing direction
        head.direction = "left"  # Set direction to left

def go_right():
    if head.direction != "left":  # Prevent reversing direction
        head.direction = "right"  # Set direction to right

# Function to move the snake
def move():
    if head.direction == "up":  # Move up
        y = head.ycor()  # Get current y-coordinate
        head.sety(y + 20)  # Increase y-coordinate by 20
    if head.direction == "down":  # Move down
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":  # Move left
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":  # Move right
        x = head.xcor()
        head.setx(x + 20)

# Set up keyboard bindings
wn.listen()  # Listen for key presses
wn.onkeypress(go_up, "8")  # Call `go_up` when '8' is pressed
wn.onkeypress(go_down, "2")  # Call `go_down` when '2' is pressed
wn.onkeypress(go_left, "4")  # Call `go_left` when '4' is pressed
wn.onkeypress(go_right, "6")  # Call `go_right` when '6' is pressed

# Main game loop
while True:
    wn.update()  # Update the screen

    # Check for collision with borders
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)  # Pause the game for 1 second
        head.goto(0, 0)  # Reset head position
        head.direction = "stop"  # Stop movement

        # Hide and reset all body segments
        for segment in segments:
            segment.goto(1000, 1000)  # Move segments off-screen
        segments.clear()  # Clear the segments list

        # Reset the score
        score = 0
        delay = 0.1  # Reset the delay to the initial value

        # Update the score display
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for collision with the food
    if head.distance(food) < 20:  # If head is close to the food
        # Move food to a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Reduce delay to increase game speed
        delay -= 0.001

        # Increase score and update high score
        score += 10
        if score > high_score:
            high_score = score

        # Update the score display
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the body segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()  # Get position of the previous segment
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)  # Move current segment to the position of the previous segment

    # Move the first segment to the head's position
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()  # Move the head

    # Check for collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:  # If head collides with any segment
            time.sleep(1)  # Pause the game for 1 second
            head.goto(0, 0)  # Reset head position
            head.direction = "stop"  # Stop movement

            # Hide and reset all body segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset the score
            score = 0
            delay = 0.1  # Reset the delay to the initial value

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)  # Control the game speed

wn.mainloop()  # Keep the window open
