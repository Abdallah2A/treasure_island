# Importing the tkinter library for GUI functionality
import tkinter as tk

# Function to start the game
def start_game():
    global background_image

    # Clear the canvas
    canvas.delete("all")

    # Change background image to the starting image
    background_image = tk.PhotoImage(file="images/left_or_right.png")
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

    # Start the first part of the story
    part_one()

# Function to handle path choice
def choose_path(path):
    if path == "left":
        game_over("You venture into a dark forest, but suddenly the ground gives way. You fall into a hidden pit.")
    else:
        part_two()

# Function to handle waiting or swimming choice
def choose_wait_swim(choice):
    if choice == "swim":
        game_over("As you swim, you feel a strange current pulling you under. Suddenly, a mysterious creature appears.")
    else:
        part_three()

# Function to handle door choice
def choose_door(door):
    if door == "red":
        game_over("As you open the red door, a burst of flames engulfs you.")
    elif door == "blue":
        game_over("You step through the blue door and find yourself face to face with mythical beasts. They vanish as quickly as they appeared.")
    else:
        victory()

# Function for the first part of the story
def part_one():
    global path_choice_frame

    # Part 1: Choose a Path
    path_choice_frame = tk.Frame(canvas, bg="")

    path_label = tk.Label(path_choice_frame, text="You find yourself at a crossroad. Which path will you take, left or right?", font=("Helvetica", 15, "bold"))
    path_label.pack(pady=10)

    left_button = tk.Button(path_choice_frame, text="Left", command=lambda: choose_path("left"), font=("Helvetica", 15, "bold"))
    left_button.pack(side=tk.LEFT, padx=10)

    right_button = tk.Button(path_choice_frame, text="Right", command=lambda: choose_path("right"), font=("Helvetica", 15, "bold"))
    right_button.pack(side=tk.RIGHT, padx=10)

    # Adjust the coordinates to place the frame directly on the canvas image
    button_window = canvas.create_window(435, 250, anchor=tk.CENTER, window=path_choice_frame)

# Function for the second part of the story
def part_two():
    global background_image
    global choose

    # Clear the canvas
    canvas.delete("all")

    # Change background image for the second part
    background_image = tk.PhotoImage(file="images/wait_swim.png")
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

    choose = tk.Frame(canvas, bg="")
    path_label = tk.Label(choose, text="You arrive at the edge of a mystical lake. In the middle, there's an island shrouded in mist.\nWait to summon the boat, or swim to brave the waters.", font=("Helvetica", 15, "bold"))
    path_label.pack(pady=10)

    wait_button = tk.Button(choose, text="Wait", command=lambda: choose_wait_swim("wait"), font=("Helvetica", 15, "bold"))
    wait_button.pack(side=tk.LEFT, padx=10)

    swim_button = tk.Button(choose, text="Swim", command=lambda: choose_wait_swim("swim"), font=("Helvetica", 15, "bold"))
    swim_button.pack(side=tk.RIGHT, padx=10)

    # Adjust the coordinates to place the frame directly on the canvas image
    button_window = canvas.create_window(435, 250, anchor=tk.CENTER, window=choose)

# Function for the third part of the story
def part_three():
    global background_image
    global choose_door_frame

    # Clear the canvas
    canvas.delete("all")

    # Change background image for the third part
    background_image = tk.PhotoImage(file="images/doors.png")
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

    choose_door_frame = tk.Frame(canvas, bg="")
    path_label = tk.Label(choose_door_frame, text="You stand before an ancient, ivy-covered house. It has three doors - red, green, blue. Which one will you choose?", font=("Helvetica", 12, "bold"))
    path_label.pack(pady=10)

    red_button = tk.Button(choose_door_frame, text="red", command=lambda: choose_door("red"), font=("Helvetica", 15, "bold"))
    red_button.pack(side=tk.LEFT, padx=10)

    green_button = tk.Button(choose_door_frame, text="green", command=lambda: choose_door("green"), font=("Helvetica", 15, "bold"))
    green_button.pack(side=tk.LEFT, padx=10)

    blue_button = tk.Button(choose_door_frame, text="blue", command=lambda: choose_door("blue"), font=("Helvetica", 15, "bold"))
    blue_button.pack(side=tk.LEFT, padx=10)

    # Adjust the coordinates to place the frame directly on the canvas image
    button_window = canvas.create_window(435, 250, anchor=tk.CENTER, window=choose_door_frame)

# Function for the victory ending
def victory():
    global result_label
    global background_image
    
    # Clear the canvas
    canvas.delete("all")

    # Change background image for the victory ending
    background_image = tk.PhotoImage(file="images/winner.png")
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

    result_label = "The golden door creaks open to reveal a room filled with unimaginable riches. Congratulations, you have found the legendary treasure."
    result_text = tk.Label(canvas, text=result_label, font=("Helvetica", 15, "bold"), wraplength=600, justify="center")
    result_text_window = canvas.create_window(435, 250, anchor=tk.CENTER, window=result_text)

    # Close the game after displaying the message
    root.after(10000, root.destroy)  # Close after 10 seconds

# Function for the game over ending
def game_over(message):
    global result_label
    global background_image
    
    # Clear the canvas
    canvas.delete("all")

    # Change background image for the game over ending
    background_image = tk.PhotoImage(file="images/gameover.png")
    
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
    result_label = message
    result_text = tk.Label(canvas, text=result_label, font=("Helvetica", 15, "bold"), wraplength=600, justify="center")
    result_text_window = canvas.create_window(435, 310, anchor=tk.CENTER, window=result_text)

    # Close the game after displaying the message
    root.after(5000, root.destroy)  # Close after 5 seconds

# Initialize the main window
root = tk.Tk()
root.title("Mysterious Treasure Island")

# Create a canvas for displaying images and text
canvas = tk.Canvas(width=871, height=652)
canvas.grid(column=0, row=0)

# Load and display the initial background image
background_image = tk.PhotoImage(file="images/map.png")
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Display welcome and game information
welcome_text = "Welcome to the Mysterious Treasure Island"
label_window = canvas.create_text(435, 100, anchor=tk.CENTER, text=welcome_text, font=("Helvetica", 25, "bold"), fill="red")
game_text = "Your quest is to uncover the fabled treasure hidden in this ancient land."
label_window = canvas.create_text(435, 200, anchor=tk.CENTER, text=game_text, font=("Helvetica", 19, "bold"), fill="red")

# Create a start button to initiate the game
start_button = tk.Button(canvas, text="Start", font=("Helvetica", 15, "bold"), command=start_game)
button_window = canvas.create_window(435, 300, anchor=tk.CENTER, window=start_button)
    
# Start the GUI event loop
root.mainloop()
