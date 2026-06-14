"""
Application: HealthMetric BMI (First Version)
Author: Callum St Clair-Newman
Course: COMP.5202 - Programming in Python
Note: Developed with AI assistance for code generation. All logic is 
      understood, reviewed, and maintained by the Author.
"""

import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        # Get user input and convert from string to decimal number
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        
        if height_cm <= 0 or weight <= 0:
            messagebox.showerror("Input Error", "Please enter positive numbers.")
            return
        
        # Convert height from centimetres to metres for the BMI formula
        height_m = height_cm / 100
        # BMI formula    
        bmi_score = round(weight / (height_m ** 2), 2)
        
        # Determine Color and Status (condition thresholds)
        if bmi_score < 18.5:
            category, color = "Underweight", "#2582CF" 
        elif bmi_score < 25:
            category, color = "Healthy Weight", "#2ECC71"
        elif bmi_score < 30:
            category, color = "Overweight", "#E67E22"
        else:
            category, color = "Obese", "#E74C3C"
            
         # Update result labels with the calculated score and matching colour
        label_result_val.config(text=bmi_score, fg=color)
        label_status_val.config(text=category, fg=color)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

#Resets the user interface to its default state when the "Clear" button is clicked.
def reset_fields():
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    label_result_val.config(text="--")
    label_status_val.config(text="--")
    


# UI Setup
root = tk.Tk()
root.title("BMI Calculator")    
root.geometry("300x400")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.resizable(False, False)

# BMI Header
tk.Label(root, text="Health Metric BMI", font=("TkDefaultFont", 14, "bold")).grid(
    row=0, columnspan=2, pady=10)

# Weight Input
tk.Label(root, text="Weight (kg):").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1, padx=10, pady=5)

# Height Input
tk.Label(root, text="Height (cm):").grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_height = tk.Entry(root)
entry_height.grid(row=2, column=1, padx=10, pady=5)

# Calculate Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid( 
    row=3, columnspan=2, pady=10)

# Clear Button 
tk.Button(root, text="Clear", command=reset_fields).grid(
    row=4, columnspan=2)

# BMI Results 
tk.Label(root, text="BMI:").grid(row=5, column=0, sticky="w", padx=10, pady=(15, 5))
label_result_val = tk.Label(root, text="--")
label_result_val.grid(row=5, column=1, sticky="w")

# BMI Category 
tk.Label(root, text="Category:").grid(row=6, column=0, sticky="w", padx=10, pady=5)
label_status_val = tk.Label(root, text="--")
label_status_val.grid(row=6, column=1, sticky="w")

root.mainloop()