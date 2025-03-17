import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be positive numbers.")
            return
        
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        
        bmi_result.config(text=f"Your BMI: {bmi:.2f}")
        health_tip = give_health_tip(bmi)
        tip_result.config(text=health_tip)
        
        plot_bmi(bmi)
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Function to give health tips based on BMI
def give_health_tip(bmi):
    if bmi < 18.5:
        return "You're underweight. Consider increasing calorie intake with nutritious food."
    elif bmi < 24.9:
        return "You're in the normal range. Keep up the good work with a balanced diet!"
    elif bmi < 29.9:
        return "You're overweight. Try to increase physical activity and monitor your diet."
    else:
        return "You're in the obese range. Consult a healthcare professional for guidance."

# Function to plot BMI categories
def plot_bmi(bmi):
    categories = ['Underweight', 'Normal', 'Overweight', 'Obese']
    bmi_ranges = [18.5, 24.9, 29.9, 40]
    colors = ['#AEC6CF', '#77DD77', '#FFB347', '#FF6961']  # Blue, Green, Orange, Red
    
    plt.figure(figsize=(10, 6))
    
    # Plot BMI categories
    plt.bar(categories, bmi_ranges, color=colors, edgecolor='black')
    
    # Mark user's BMI
    plt.axhline(y=bmi, color='blue', linestyle='--', label=f'Your BMI: {bmi:.2f}')
    
    # Mark average BMI
    avg_bmi = 23
    plt.axhline(y=avg_bmi, color='green', linestyle=':', label=f'Avg BMI: {avg_bmi}')
    
    # Add BMI values on top of bars
    for i, value in enumerate(bmi_ranges):
        plt.text(i, value - 3, f'{value:.1f}', ha='center', color='black', fontsize=10)
    
    plt.title('BMI Categories', fontsize=16)
    plt.ylabel('BMI Value', fontsize=12)
    plt.legend()
    
    # Save the plot
    plt.savefig('bmi_chart.png')
    print("BMI chart saved as 'bmi_chart.png'")
    
    plt.show()

# Function to clear input fields and results
def clear_fields():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    bmi_result.config(text="")
    tip_result.config(text="")

# Create the GUI window
root = Tk()
root.title("BMI Calculator")
root.geometry("400x300")
root.configure(bg="#f4f4f4")

# Labels and Input fields
Label(root, text="Weight (in kg):", font=("Arial", 12), bg="#f4f4f4").place(x=30, y=30)
weight_entry = Entry(root, font=("Arial", 12))
weight_entry.place(x=180, y=30)

Label(root, text="Height (in cm):", font=("Arial", 12), bg="#f4f4f4").place(x=30, y=70)
height_entry = Entry(root, font=("Arial", 12))
height_entry.place(x=180, y=70)

# Button to calculate BMI
Button(root, text="Calculate BMI", font=("Arial", 12), bg="#77DD77", fg="black", command=calculate_bmi).place(x=60, y=120)

# Button to clear fields
Button(root, text="Clear", font=("Arial", 12), bg="#FF6961", fg="black", command=clear_fields).place(x=200, y=120)

# Labels to show results
bmi_result = Label(root, text="", font=("Arial", 14, "bold"), fg="#333333", bg="#f4f4f4")
bmi_result.place(x=30, y=170)

tip_result = Label(root, text="", font=("Arial", 12), fg="#555555", wraplength=340, bg="#f4f4f4", justify=LEFT)
tip_result.place(x=30, y=200)

# Start the GUI event loop
root.mainloop()
