from model import ShuffleRandomizer, GroupRandomizer
from tkinter import Text

def enterBtn(entry_1: Text, entry_2: Text, shuffle_option: str):
    # Get input from entry_1
    input_text = entry_1.get("1.0", "end-1c")
    # Split input by commas and remove any extra whitespace
    inputs = [item.strip() for item in input_text.split(",") if item.strip()]
    
    if shuffle_option == "Multiple Output":
        # Use GroupRandomizer to randomize the inputs by pairs
        randomizer = GroupRandomizer()
        randomizer.add_inputs(inputs)
        randomizer.set_group_size(2)
        results = randomizer.generate_groups()
        # Flatten the list of pairs for display
        results = [", ".join(map(str, group)) for group in results]
        # Display the results in entry_2
        entry_2.delete("1.0", "end")
        entry_2.insert("1.0", "\n".join(map(str, results)))
    else:
        # Use ShuffleRandomizer to randomize the inputs
        randomizer = ShuffleRandomizer()
        randomizer.add_inputs(inputs)
        results = randomizer.shuffle_items()
        # Display the results in entry_2 horizontally, separated by commas
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
