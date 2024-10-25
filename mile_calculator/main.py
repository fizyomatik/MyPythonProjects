from tkinter import *


window = Tk()
window.minsize(width=500, height=400)
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)


# Miles Label

m_label = Label()
m_label.config(text="Miles")
m_label.grid(column = 5 , row = 2)

# Km Label
k_label = Label()
k_label.config(text="Km")
k_label.grid(column = 5, row =3)

# Label to "is equal to"
is_label = Label()
is_label.config(text="is equal to")
is_label.grid(column = 0, row = 3)

# Entry for miles
mile_input =Entry(width=20)
mile_input.grid(column = 2, row = 2)

# Label for km
km_input =Label( text="0")
km_input.grid(column = 2, row = 3)
km_input.config()


def button_clicked():
    miles = float(mile_input.get())
    km = miles * 1.609
    km_input.config(text=km)


# Button
calculate_button = Button(text="Calculate",command=button_clicked)
calculate_button.grid(column = 2, row = 5)



window.mainloop()
