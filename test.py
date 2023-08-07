
from customtkinter import *
import json

import tkinter as tk

# Create a list to store tkinter widgets
widget_list = []

# Create a Tkinter window
root = tk.Tk()
root.title("Tkinter Widget List Example")

#import tkinter as tk

# Example data (replace this with your actual bank dictionary)
bank = {
    "Question": [
        {"name": "Question 1", "option1": "Option 1", "option2": "Option 2", "option3": "Option 3", "answer": "Option 1"},
        {"name": "Question 2", "option1": "Option A", "option2": "Option B", "option3": "Option C", "answer": "Option C"},
        # Add more questions here...
    ]
}

# Create a list to store tkinter widgets
widget_list = []

# Create a Tkinter window
master = tk.Tk()

# Function to create and append a radio button with the given text to the widget_list
def add_radio_button(text):
    radio_button = tk.Radiobutton(master, text=text)
    radio_button.pack()
    widget_list.append(radio_button)

# Loop through the questions in the bank and create radio buttons for each question
for question in bank["Question"]:
    add_radio_button(question["name"])
    add_radio_button(question["option1"])
    add_radio_button(question["option2"])
    add_radio_button(question["option3"])
    add_radio_button(question["answer"])

# Run the Tkinter main loop
    """ widget_list = []
   Q = add_label_lambdaname = lambda: widget_list.append(CTkRadioButton(master, text=question["name"]))
   o1 = add_label_lambdao1 = lambda: widget_list.append(CTkRadioButton(master, text=question["option1"]))
   o2 = add_label_lambdao2 = lambda: widget_list.append(CTkRadioButton(master, text=question["option2"]))
   o3 = add_label_lambdao3 = lambda: widget_list.append(CTkRadioButton(master, text=question["option3"]))
   a = add_label_lambdao4 = lambda: widget_list.append(CTkRadioButton(master, text=question["answer"]))
   print(widget_list)"""

# Print the widget list
x=5

print(x)
x+=1
print(x)
