import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Slider Demo')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# slider current x value
current_x_value = tk.DoubleVar()


def get_current_x_value():
    return 'length {: .2f}'.format(current_x_value.get())


def slider_x_changed(event):
    value_label_x.configure(text=get_current_x_value())


# slider current y value
current_y_value = tk.DoubleVar()


def get_current_y_value():
    return 'height {: .2f}'.format(current_y_value.get())


def slider_y_changed(event):
    value_label_y.configure(text=get_current_y_value())


# label for the slider x
slider_label_x = ttk.Label(
    root,
    text='Slider length:'
)

slider_label_x.grid(
    column=0,
    row=0,
    sticky='w'
)

#  slider x
slider_x = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_x_changed,
    variable=current_x_value
)

slider_x.grid(
    column=1,
    row=0,
    sticky='we'
)

# current value label
current_value_label = ttk.Label(
    root,
    text='Current Value:'
)

current_value_label.grid(
    row=5,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label x
value_label_x = ttk.Label(
    root,
    text=get_current_x_value()
)
value_label_x.grid(
    row=2,
    columnspan=2,
    sticky='n'
)

# label for the slider y
slider_label_y = ttk.Label(
    root,
    text='Slider height:'
)

slider_label_y.grid(
    column=0,
    row=1,
    sticky='w'
)

#  slider y
slider_y = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_y_changed,
    variable=current_y_value
)

slider_y.grid(
    column=1,
    row=1,
    sticky='we'
)

# value label y
value_label_y = ttk.Label(
    root,
    text=get_current_y_value()
)
value_label_y.grid(
    row=4,
    columnspan=2,
    sticky='n'
)

root.mainloop()
