import tkinter as tk

def calculate_bill():
    try:
        total_number_of_person = int(entry_number_of_person.get())
        total_bill = float(entry_total_bill.get())
        if total_number_of_person <= 0 or total_bill <= 0:
            raise ValueError("Number of people and total bill must be positive numbers.")
        gst = 0.06
        total_bill = (total_bill * gst) + total_bill
        total_bill = total_bill / total_number_of_person
        label_result.config(text=f"Each should pay: ${total_bill:.2f}")
    except ValueError as e:
        label_result.config(text=f"Invalid input! Please enter a valid number. Error: {e}")

def clear_fields():
    entry_number_of_person.delete(0, tk.END)
    entry_total_bill.delete(0, tk.END)
    label_result.config(text="")

root = tk.Tk()
root.title("Bill Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_number_of_person = tk.Label(frame, text="Enter number of person:")
label_number_of_person.grid(row=0, column=0, padx=(0, 10))
entry_number_of_person = tk.Entry(frame)
entry_number_of_person.grid(row=0, column=1)

label_total_bill = tk.Label(frame, text="Total:")
label_total_bill.grid(row=1, column=0, padx=(0, 10))
entry_total_bill = tk.Entry(frame)
entry_total_bill.grid(row=1, column=1)

button_calculate = tk.Button(frame, text="Calculate", command=calculate_bill, bg="green")
button_calculate.grid(row=2, column=0, columnspan=2, pady=(10, 0))

button_clear = tk.Button(frame, text="Clear", command=clear_fields, bg="orange")
button_clear.grid(row=3, column=0, columnspan=2, pady=(5, 0))

button_quit = tk.Button(frame, text="Quit", command=root.quit, bg="red")
button_quit.grid(row=4, column=0, columnspan=2, pady=(5, 0))

label_result = tk.Label(frame, text="")
label_result.grid(row=5, column=0, columnspan=2, pady=(10, 0))

root.mainloop()