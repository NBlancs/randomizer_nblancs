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