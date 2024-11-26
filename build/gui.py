
# Notes:
    # Button 1 kay Enter Button
    # Button 2 kay Settings Button
    # Button 3 kay Shuffle Button
        # Note: Please Make this a drop down
        # Add options (Single Output, Multiple Output, Group Output)
    # Button 4 kay Clear Button


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Menu
from controller import enterBtn,shuffleBtn,clearBtn,settingsBtn
from model import Randomizer, GroupRandomizer,OutputGenerator,Preferences,ShuffleRandomizer, ResultDisplay


# Please Change the asset path accordingly if you are accessing from a different device
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\Programming Files\OOP PIT\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("720x760")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 760,
    width = 720,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_4.png"))

# Clear Button
# Edit Here
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= clearBtn, # Please Edit the method in controller.py
    relief="flat"
)
button_1.place(
    x=270.0,
    y=681.0,
    width=180.0,
    height=50.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    360.0,
    205.0,
    image=image_image_1
)

# Text Area 1
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    360.0,
    205.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=165.0,
    y=135.0,
    width=390.0,
    height=138.0
)

# Text Area 2
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    360.0,
    594.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=165.0,
    y=524.0,
    width=390.0,
    height=138.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    360.0,
    37.0,
    image=image_image_2
)

canvas.create_text(
    330.0,
    92.0,
    anchor="nw",
    text="INPUT ",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    262.0,
    17.0,
    anchor="nw",
    text="RANDOMIZER",
    fill="#000000",
    font=("Inter", 24 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    443.0,
    33.0,
    image=image_image_3
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))

# Settings Button
# Edit Here
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=settingsBtn, # Please Edit the method in controller.py
    relief="flat"
)
button_2.place(
    x=459.0,
    y=310.0,
    width=32.0,
    height=32.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))

# Shuffle Button
# Edit Here
def open_shuffle_menu(event):
    shuffle_menu = Menu(window, tearoff=0)
    shuffle_menu.add_command(label="Single Output", command=lambda: print("Single Output selected"))
    shuffle_menu.add_command(label="Multiple Output", command=lambda: print("Multiple Output selected"))
    shuffle_menu.add_command(label="Group Output", command=lambda: print("Group Output selected"))
    shuffle_menu.post(event.x_root, event.y_root)

button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_3.place(
    x=270.0,
    y=300.0,
    width=180.0,
    height=50.0
)

# Bind the button click to show the dropdown menu
button_3.bind("<Button-1>", open_shuffle_menu)

canvas.create_text(
    323.0,
    485.0,
    anchor="nw",
    text="RESULT",
    fill="#000000",
    font=("Inter", 20 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    360.0,
    594.0,
    image=image_image_4
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_1.png"))

# Clear Button
# Edit Here
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=enterBtn, # Please Edit method in controller.py
    relief="flat"
)
button_4.place(
    x=270.0,
    y=393.0,
    width=180.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()
