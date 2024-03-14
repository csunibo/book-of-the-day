import tkinter as tk
from PIL import ImageTk, Image
import os
import random

# Directory containing images
img_dir = 'img'

# Get list of files in the directory
img_files = os.listdir(img_dir)

# Filter out directories if any
img_files = [file for file in img_files if os.path.isfile(os.path.join(img_dir, file))]

# Select a random image file
random_img = random.choice(img_files)

# Full path to the randomly selected image
random_img_path = os.path.join(img_dir, random_img)

# Create a Tkinter window
window = tk.Tk()
window.title("Display Image")

# Make the window full size
window.attributes('-fullscreen', True)

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Load the image

img = Image.open(random_img_path)

# Resize image to fit the screen while maintaining aspect ratio
img.thumbnail((screen_width, screen_height))

# Convert image for Tkinter
img = ImageTk.PhotoImage(img)

# Create a text to display
text = tk.Label(window, text="Today recommended read, to improve your Informatics skill, is:", font=("Comic Sans MS", 40, "bold"))
text.pack()

# Create a label to display the image
label = tk.Label(window, image=img)
label.pack(fill=tk.BOTH, expand=tk.YES)

# Bind escape key to exit fullscreen
window.bind('<Escape>', lambda event: window.attributes('-fullscreen', False))


print(random_img_path)
# Run the Tkinter event loop
window.mainloop()

