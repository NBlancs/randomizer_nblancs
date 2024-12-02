from model import Randomizer, GroupRandomizer,OutputGenerator,Preferences,ShuffleRandomizer, ResultDisplay
from tkinter import Menu, Text

def enterBtn(entry_1: Text, entry_2: Text):
    # Get input from entry_1
    input_text = entry_1.get("1.0", "end-1c")
    # Split input by commas and remove any extra whitespace
    inputs = [item.strip() for item in input_text.split(",") if item.strip()]
    
    # Use ShuffleRandomizer to randomize the inputs
    randomizer = ShuffleRandomizer()
    randomizer.add_inputs(inputs)
    results = randomizer.shuffle_items()
    
    # Display the results in entry_2
    entry_2.delete("1.0", "end")
    entry_2.insert("1.0", ", ".join(map(str, results)))

def shuffleBtn():
    print("Shuffle Button Clicked From controller")

def settingsBtn():
    print("Settings Button Clicked from controller")

def clear_text_area(entry: Text):
    entry.delete('1.0', 'end')

def clearBtn(entry: Text):
    clear_text_area(entry)
