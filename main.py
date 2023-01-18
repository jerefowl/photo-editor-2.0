import tkinter

from PIL import ImageTk, Image, ImageEnhance


root = tkinter.Tk()
root.title("Photo Editor GUI")

root.geometry("1000x750")

menuFrame = tkinter.Frame(root)
menuFrame = tkinter.Frame(root, width=600, height=400)
menuFrame.grid(row=0, column=0, sticky='W')

frame = tkinter.Frame(root)
frame = tkinter.Frame(root, width=600, height=400)
frame.grid(row=1, column=0)

image = Image.open("mountain.jpg")
img = ImageTk.PhotoImage(image)

label = tkinter.Label(frame, image=img)
label.grid(row=0, column=0)

var = tkinter.StringVar()
prompt = tkinter.Label(menuFrame, textvariable=var)
prompt.grid(row=0, column=0)
var.set("Choose an edit option, and Click GO:")

Lb1 = tkinter.Listbox(menuFrame)
Lb1.insert(1, "crop")
Lb1.insert(2, "change color")
Lb1.insert(3, "rotate")
Lb1.insert(4, "enhance")
Lb1.insert(5, "change file type")
Lb1.grid(row=1, column=0, sticky=tkinter.W)


def on_button_click():
    choice_num = Lb1.curselection()
    # destroy all widgets from frame
    for widget in menuFrame.winfo_children():
        widget.destroy()

    row = 0
    editImage = image

    subVar = tkinter.StringVar()
    subPrompt = tkinter.Label(menuFrame, textvariable=subVar)
    subPrompt.grid(row=row, column=0)
    row += 1

    if choice_num[0] == 0:
        subVar.set("What dimensions for cropping?")

        leftLabel = tkinter.Label(menuFrame, textvariable=tkinter.StringVar(value="Left:"))
        leftLabel.grid(row=row, column=0, sticky=tkinter.W)
        leftEntry = tkinter.Entry(menuFrame)
        leftEntry.grid(row=row, column=1)
        row += 1

        upperLabel = tkinter.Label(menuFrame, textvariable=tkinter.StringVar(value="Upper:"))
        upperLabel.grid(row=row, column=0, sticky=tkinter.W)
        upperEntry = tkinter.Entry(menuFrame)
        upperEntry.grid(row=row, column=1)
        row += 1

        rightLabel = tkinter.Label(menuFrame, textvariable=tkinter.StringVar(value="Right:"))
        rightLabel.grid(row=row, column=0, sticky=tkinter.W)
        rightEntry = tkinter.Entry(menuFrame)
        rightEntry.grid(row=row, column=1)
        row += 1

        lowerLabel = tkinter.Label(menuFrame, textvariable=tkinter.StringVar(value="Lower:"))
        lowerLabel.grid(row=row, column=0, sticky=tkinter.W)
        lowerEntry = tkinter.Entry(menuFrame)
        lowerEntry.grid(row=row, column=1)
        row += 1

        def on_crop():
            box = (int(leftEntry.get()), int(upperEntry.get()), int(rightEntry.get()), int(lowerEntry.get()))
            cropImage = image.crop(box)
            cropImage.show()

        button = tkinter.Button(menuFrame, text="GO", command=on_crop)
        button.grid(row=row, column=0, sticky=tkinter.W)
        row += 1

    if choice_num[0] == 1:
        subVar.set("How would you like to change the image?")

        redLabel = tkinter.Label(menuFrame, textvariable=tkinter.StringVar(value="Red:"))
        redLabel.grid(row=row, column=0, sticky=tkinter.W)
        redEntry = tkinter.Entry(menuFrame)
        redEntry.grid(row=row, column=1)
        row += 1

        greenLabel = tkinter.Label(menuFrame, textvariable=tkinter.StringVar(value="Green:"))
        greenLabel.grid(row=row, column=0, sticky=tkinter.W)
        greenEntry = tkinter.Entry(menuFrame)
        greenEntry.grid(row=row, column=1)
        row += 1

        blueLabel = tkinter.Label(menuFrame, textvariable=tkinter.StringVar(value="Blue:"))
        blueLabel.grid(row=row, column=0, sticky=tkinter.W)
        blueEntry = tkinter.Entry(menuFrame)
        blueEntry.grid(row=row, column=1)
        row += 1

        def on_RGB():
            new_red = redEntry.get()
            new_green = greenEntry.get()
            new_blue = blueEntry.get()

            red, green, blue = image.split()
            swap_red = red
            swap_green = green
            swap_blue = blue

            if new_red == "red":
                swap_red = red
            elif new_red == "green":
                swap_red = green
            elif new_red == "blue":
                swap_red = blue

            if new_green == "red":
                swap_green = red
            elif new_green == "green":
                swap_green = green
            elif new_green == "blue":
                swap_green = blue

            if new_blue == "red":
                swap_blue = red
            elif new_blue == "green":
                swap_blue = green
            elif new_blue == "blue":
                swap_blue = blue

            new_image = Image.merge("RGB", (swap_red, swap_green, swap_blue))
            new_image.show()

        button = tkinter.Button(menuFrame, text="GO", command=on_RGB)
        button.grid(row=row, column=0, sticky=tkinter.W)
        row += 1

    if choice_num[0] == 2:
        subVar.set("How many degrees would you like to rotate the image?")

        degreesLabel = tkinter.Label(menuFrame, textvariable=tkinter.StringVar(value="Degrees:"))
        degreesLabel.grid(row=row, column=0, sticky=tkinter.W)
        degreesEntry = tkinter.Entry(menuFrame)
        degreesEntry.grid(row=row, column=1)
        row += 1

        def on_rotate():
            rot_deg = int(degreesEntry.get())
            new_image = image.rotate(rot_deg)
            new_image.show()

        button = tkinter.Button(menuFrame, text="GO", command=on_rotate)
        button.grid(row=row, column=0, sticky=tkinter.W)
        row += 1

    if choice_num[0] == 3:
        subVar.set("How would you like to change the image?")

        contrastLabel = tkinter.Label(menuFrame, textvariable=tkinter.StringVar(value="Contrast:"))
        contrastLabel.grid(row=row, column=0, sticky=tkinter.W)
        contrastEntry = tkinter.Entry(menuFrame)
        contrastEntry.grid(row=row, column=1)
        row += 1

        def on_enhance():
            contrast_factor = float(contrastEntry.get())
            contrast = ImageEnhance.Contrast(image)
            contrast_image = contrast.enhance(contrast_factor)
            contrast_image.show()

        button = tkinter.Button(menuFrame, text="GO", command=on_enhance)
        button.grid(row=row, column=0, sticky=tkinter.W)
        row += 1

    if choice_num[0] == 4:
        subVar.set("Enter a new filename with type extension")

        filenameLabel = tkinter.Label(menuFrame, textvariable=tkinter.StringVar(value="Filename:"))
        filenameLabel.grid(row=row, column=0, sticky=tkinter.W)
        filenameEntry = tkinter.Entry(menuFrame)
        filenameEntry.grid(row=row, column=1)
        row += 1

        def on_filename():
            new_filename = filenameEntry.get()
            image.save(new_filename)
            new_image = Image.open(new_filename)
            new_image.show()

        button = tkinter.Button(menuFrame, text="GO", command=on_filename)
        button.grid(row=row, column=0, sticky=tkinter.W)
        row += 1


button = tkinter.Button(menuFrame, text="GO", command=on_button_click)
button.grid(row=2, column=0, sticky=tkinter.W)

root.mainloop()
