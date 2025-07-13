import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        input_scale = combo_from.get()
        output_scale = combo_to.get()

        # Convert input to Celsius first
        if input_scale == "Celsius":
            celsius = temp
        elif input_scale == "Fahrenheit":
            celsius = (temp - 32) * 5/9
        elif input_scale == "Kelvin":
            celsius = temp - 273.15

        # Convert from Celsius to output scale
        if output_scale == "Celsius":
            result = celsius
        elif output_scale == "Fahrenheit":
            result = (celsius * 9/5) + 32
        elif output_scale == "Kelvin":
            result = celsius + 273.15

        label_result.config(text=f"Result: {result:.2f} {output_scale}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x250")

# Input temperature
label_temp = tk.Label(root, text="Enter Temperature:")
label_temp.pack(pady=5)
entry_temp = tk.Entry(root)
entry_temp.pack(pady=5)

# From scale
label_from = tk.Label(root, text="From:")
label_from.pack(pady=5)
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_from.pack(pady=5)
combo_from.current(0)

# To scale
label_to = tk.Label(root, text="To:")
label_to.pack(pady=5)
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_to.pack(pady=5)
combo_to.current(1)

# Convert button
btn_convert = tk.Button(root, text="Convert", command=convert_temperature)
btn_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result:")
label_result.pack(pady=5)

root.mainloop()
