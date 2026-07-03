from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Denomination Calculator - Step 1")
window.geometry("500x500")
window.configure(bg = "#F94EC3")

image = Image.open("Icon.png")
image = image.resize((200, 200))

my_image = ImageTk.PhotoImage(image)

label_1 = Label(window, image = my_image)
label_1.pack(side = TOP)

label_2 = Label(window, text = "Welcome to the Denomination Calculator Application!", fg = "#000000")
label_2.pack(side = TOP)

def message():
    my_message = messagebox.showinfo("Confirmation", "Are you sure buddy?")
    
    if my_message == "ok":
        top_window()

my_button = Button(window, text = "Confirm", command = message, bg = "#FF00BB", fg = "#000000")
my_button.pack(side = TOP)

def top_window():
    top = Toplevel()
    top.title("Denomination Calculation")
    top.geometry("600x350")
    top.configure(bg = "#9900FF")
    
    amount_label = Label(top, text = "Enter the amount:", fg = "#000000")
    amount_entry = Entry(top)

    label_3 = Label(top, text = "Here are the number of notes for each denomination:")

    l1 = Label(top, text = "500")
    l2 = Label(top, text = "200")
    l3 = Label(top, text = "100")

    e1 = Entry(top)
    e2 = Entry(top)
    e3 = Entry(top)

    def calculator():
        try:
            amount = int(amount_entry.get())

            note_500 = amount // 500
            amount %= 500

            note_200 = amount // 200
            amount %= 200

            note_100 = amount // 100

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)

            e1.insert(END, str(note_500))
            e2.insert(END, str(note_200))
            e3.insert(END, str(note_100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    button = Button(top, text="Calculate", command=calculator, bg="#7B00FF", fg="#000000")

    amount_label.place(x=230, y=50)
    amount_entry.place(x=200, y=80)
    button.place(x=240, y=120)

    label_3.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    e1.place(x=270, y=200)
    e2.place(x=270, y=230)
    e3.place(x=270, y=260)

    top.mainloop()

window.mainloop()
