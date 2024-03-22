import os
import random
import time
import tkinter as tk

import schedule
from PIL import Image, ImageTk

# Directory containing images
img_dir = os.getenv("IMG_FOLDER", "img")


def choseRandomImg() -> str:
    # Get list of files in the directory
    img_files = os.listdir(img_dir)

    # Filter out directories if any
    img_files = [
        file for file in img_files if os.path.isfile(os.path.join(img_dir, file))
    ]

    # Select a random image file
    random_img = random.choice(img_files)

    # Full path to the randomly selected image
    return os.path.join(img_dir, random_img)


random_img_path = choseRandomImg()
# Create a Tkinter window
window = tk.Tk()
window.title("Display Image")

# Make the window full size
window.attributes("-fullscreen", True)

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Load the image
img = Image.open(random_img_path)

# Resize image to fit the screen while maintaining aspect ratio
img.thumbnail((500, 700))

# Convert image for Tkinter
img = ImageTk.PhotoImage(img)

# Create a text to display
text = tk.Label(
    window,
    text="Today recommended read, to improve your Informatics skill, is:",
    font=("Comic Sans MS", 40, "bold"),
    fg="white",
    bg="#02111B",
)
text.pack()

# Create a label to display the image
label = tk.Label(window, image=img, background="#02111B")
label.pack(fill=tk.BOTH, expand=tk.YES)

# Bind escape key to exit fullscreen
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))


# Run the Tkinter event loop
window.update()


def update_book():
    print("cambio")
    img = Image.open(choseRandomImg())
    # img.resize((500, 700))
    # Resize image to fit the screen while maintaining aspect ratio
    img.thumbnail((500, 700))

    # Convert image for Tkinter
    img = ImageTk.PhotoImage(img)

    label.configure(image=img)
    label.image = img
    window.update()


# schedule.every(20).seconds.do(update_book)
schedule.every().day.at("03:00").do(update_book)
while True:
    schedule.run_pending()
    time.sleep(5)
