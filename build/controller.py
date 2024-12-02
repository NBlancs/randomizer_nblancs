from model import Randomizer, GroupRandomizer,OutputGenerator,Preferences,ShuffleRandomizer, ResultDisplay
from tkinter import Menu, Text

def enterBtn():
    print("Enter Button Clicked From controller")

def shuffleBtn():
    print("Shuffle Button Clicked From controller")

def settingsBtn():
    print("Settings Button Clicked from controller")

def clear_text_area(entry: Text):
    entry.delete('1.0', 'end')

def clearBtn(entry: Text):
    clear_text_area(entry)
