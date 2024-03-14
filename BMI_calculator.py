import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BMI_Calculator:
    def __init__(nit, master):
        nit.master = master
        nit.master.title("BMI Calculator")

        # Here The Heading label
        nit.label = tk.Label(master, text="BMI Calculator", bg='green',font=("Helvetica", 16, "bold"))
        nit.label.place(x=100,y=20,height=60,width=400)

        # Here The Weight entry
        nit.label_weight = tk.Label(master, text="Weight (kg):",bg='yellow',font="Times 16 italic bold")
        nit.label_weight.place(x=120,y=120,width=150)
        nit.entry_weight = tk.Entry(master)
        nit.entry_weight.place(x=280,y=120,height=30,width=150)

        # Here The Height entry
        nit.label_height = tk.Label(master, text="Height (m):",bg='light blue',font="Times 16 italic bold")
        nit.label_height.place(x=120,y=160,width=150)
        nit.entry_height = tk.Entry(master)
        nit.entry_height.place(x=280,y=160,height=30,width=150)

        # Here The Create Calculate button
        nit.button_calculate = tk.Button(master, text="Calculate BMI", command=nit.calculate_bmi)
        nit.button_calculate.place(x=200,y=220,height=30,width=150)

    def calculate_bmi(nit):
        try:
            weight = float(nit.entry_weight.get())
            height = float(nit.entry_height.get())
            bmi = weight / (height ** 2)
            category = nit.classify_bmi(bmi)
            messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}\nYou are classified as: {category}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid weight and height.")

    def classify_bmi(nit, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

def main():
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.minsize(550,600)
    root.config(bg='pink')
    root.mainloop()

if __name__ == "__main__":
    main()
