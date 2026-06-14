"""
Application: HealthMetric BMI (Final Version)
Author: Callum St Clair-Newman
Course: COMP.5202 - Programming in Python
Note: Developed with AI assistance for code generation. All logic is 
      understood, reviewed, and maintained by the Author.
"""

import tkinter as tk
from tkinter import messagebox

def update_unitsystem():
    # Toggles labels and dynamically hides/shows the inches field based on unit system
    if unit_system.get() == "metric":
        label_weight.config(text="Weight (kg):")
        label_height.config(text="Height (cm):")
        entry_height_in.delete(0, tk.END)
        # Hide the inches field from view completely
        entry_height_in.grid_forget()
    else:
        label_weight.config(text="Weight (lbs):")
        label_height.config(text="Height (ft / in):")
        # Puts the inches field to the right of the feet entry field
        entry_height_in.grid(row=0, column=1, padx=5)

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        val1 = float(entry_height.get())
        
        # Pull inches safely if in imperial mode
        inches_text = entry_height_in.get().strip()
        # Only attempt to convert inches if in imperial mode and the field isn't empty, otherwise default to 0
        val2 = float(inches_text) if (unit_system.get() == "imperial" and inches_text) else 0.0

        if weight <= 0 or val1 <= 0 or val2 < 0:
            messagebox.showerror("Input Error", "Please enter valid positive numbers.")
            return

        # Calculate score based on unit system
        if unit_system.get() == "metric":
            bmi_score = round(weight / ((val1 / 100) ** 2), 2)
        else:
            total_inches = (val1 * 12) + val2
            bmi_score = round((weight / (total_inches ** 2)) * 703, 2)
        
        # Determine Category and Color
        if bmi_score < 18.5:
            category, color = "Underweight", "#2582CF"
        elif bmi_score < 25:
            category, color = "Healthy Weight", "#2ECC71"
        elif bmi_score < 30:
            category, color = "Overweight", "#E67E22"
        else:
            category, color = "Obese", "#E74C3C"
            
        # Update Display
        label_result_val.config(text=bmi_score, fg=color)
        label_status_val.config(text=category, fg=color)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers into the fields.")

def reset_fields():
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    entry_height_in.delete(0, tk.END)
    label_result_val.config(text="--", fg="#475569") # Resets to grey color
    label_status_val.config(text="--", fg="#475569")
    update_unitsystem()


# UI Setup 
root = tk.Tk()
root.title("BMI Calculator")    
root.geometry("340x540") 
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.resizable(False, False)
root.configure(bg="#F1F5F9") # light grey window background

# BMI Header
tk.Label(root, text="Health Metric BMI", font=("TkDefaultFont", 14, "bold"), 
         bg="#F1F5F9", fg="#1E293B").grid(row=0, columnspan=2, pady=15)

# Unit Selection Buttons 
unit_system = tk.StringVar(value="metric")
tk.Radiobutton(root, text="Metric", variable=unit_system, value="metric", font=("TkDefaultFont", 10, "bold"),
bg="#F1F5F9", fg="#475569", activebackground="#F1F5F9", command=update_unitsystem).grid(row=1, column=0, pady=5)

tk.Radiobutton(root, text="Imperial", variable=unit_system, value="imperial", font=("TkDefaultFont", 10, "bold"),
bg="#F1F5F9", fg="#475569", activebackground="#F1F5F9", command=update_unitsystem).grid(row=1, column=1, pady=5)

# Weight Input
label_weight = tk.Label(root, text="Weight (kg):", bg="#F1F5F9", fg="#475569", font=("TkDefaultFont", 10, "bold"))
label_weight.grid(row=2, column=0, sticky="w", padx=25, pady=10)
entry_weight = tk.Entry(root, width=18, bg="white", relief="solid", bd=1)
entry_weight.grid(row=2, column=1, sticky="w", padx=10, pady=10)

# Height Input Container (Hosts both cm and ft/in fields together for clean toggling)
label_height = tk.Label(root, text="Height (cm):", bg="#F1F5F9", fg="#475569", font=("TkDefaultFont", 10, "bold"))
label_height.grid(row=3, column=0, sticky="w", padx=25, pady=10)

height_frame = tk.Frame(root, bg="#F1F5F9")
height_frame.grid(row=3, column=1, sticky="w", padx=10, pady=10)

entry_height = tk.Entry(height_frame, width=7, bg="white", relief="solid", bd=1)
entry_height.grid(row=0, column=0)

# Secondary height field (inches) Hosted together inside the sub-container
entry_height_in = tk.Entry(height_frame, width=5, bg="white", relief="solid", bd=1)

# Calculate Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi, 
bg="#0284C7", fg="white", activebackground="#0369A1", activeforeground="white",
font=("TkDefaultFont", 11, "bold"), bd=1).grid(row=4, columnspan=2, pady=(20, 5), sticky="ew", padx=25, ipady=4)

# Clear Button 
tk.Button(root, text="Clear", command=reset_fields, 
bg="#9B1F1F", fg="white", activebackground="#9B1F1F",
font=("TkDefaultFont", 10, "bold"), bd=1).grid(row=5, columnspan=2, pady=5, sticky="ew", padx=25, ipady=4)

# BMI Results 
tk.Label(root, text="BMI:", bg="#F1F5F9", fg="#64748B", font=("TkDefaultFont", 11, "italic")).grid(row=6, column=0, sticky="w", padx=25, pady=(20, 5))
label_result_val = tk.Label(root, text="--", font=("TkDefaultFont", 12, "bold"), bg="#F1F5F9", fg="#475569")
label_result_val.grid(row=6, column=1, sticky="w", padx=10, pady=(20, 5))

# BMI Category 
tk.Label(root, text="Category:", bg="#F1F5F9", fg="#64748B", font=("TkDefaultFont", 11, "italic")).grid(row=7, column=0, sticky="w", padx=25, pady=5)
label_status_val = tk.Label(root, text="--", font=("TkDefaultFont", 12, "bold"), bg="#F1F5F9", fg="#475569")
label_status_val.grid(row=7, column=1, sticky="w", padx=10, pady=5)

# Reference Chart
tk.Label(root, text="— BMI Reference Chart —", font=("TkDefaultFont", 9, "bold", "italic"), bg="#F1F5F9", fg="#94A3B8").grid(
    row=8, columnspan=2, pady=(25, 5))

tk.Label(root, text="Underweight: < 18.5\nHealthy Weight: 18.5 – 24.9\nOverweight / Obese: 25.0+", 
         font=("TkDefaultFont", 9, "bold"), bg="#F1F5F9", fg="#64748B", justify="center").grid(row=9, columnspan=2, pady=(0, 20))

root.mainloop()