import tkinter as tk

def calculate_metrics():
    # Get user inputs
    age = int(age_entry.get())
    cholesterol = float(cholesterol_entry.get())
    max_heart_rate = int(max_heart_rate_entry.get())
    gender = gender_var.get()

    # Calculate health metrics (you can replace this with your actual logic)
    # Example: Calculate risk factors based on age, cholesterol, and heart rate

    # Display the results (you can customize this part)
    result_label.config(text= f"Gender: {'Male' if gender == 0 else 'Female'}\n"
                              f"Age: {age} years\n"
                              f"Cholesterol: {cholesterol} mg/dL\n"
                              f"Max Heart Rate: {max_heart_rate} bpm")

# Create the main window
window = tk.Tk()
window.title("Health Metrics Calculator")
window.geometry("400x300")

# Labels
Age_label = tk.Label(window, text="Age:")
RestingBP_label = tk.Label(window, text="RestingBP:")
Cholesterol_label = tk.Label(window, text="Cholesterol (mg/dL):")
FastingBS_label = tk.Label(window, text="Fasting BS:")
MaxHR_label = tk.Label(window, text="Max Heart Rate (bpm):")
Oldpeak_label = tk.Label(window, text="Oldpeak:")
Gender_label  = tk.Label(window, text="Gender:")
ChestPainType_label = tk.Label(window, text="Chest Pain Type:")
RestingECG_label = tk.Label(window, text="Resting ECG:")
ExerciseAngina_label = tk.Label(window, text="Exercise_angina:")
ST_Slope_label = tk.Label(window, text="ST Slope type:")

# Entry fields
Age = tk.Entry(window)
RestingBP = tk.Entry(window)
Cholesterol = tk.Entry(window)
FastingBS = tk.Entry(window)
MaxHR = tk.Entry(window)
Oldpeak = tk.Entry(window)

# Gender toggle switch
gender_var = tk.IntVar()
Sex_M_label = tk.Radiobutton(window, text="Male", variable=gender_var, value=1)
Sex_F_label = tk.Radiobutton(window, text="Female", variable=gender_var, value=2)

# chest pain toggle switch
ChestPainType_var=tk.IntVar()
ChestPainType_ASY_label = tk.Radiobutton(window, text="ASY", variable=ChestPainType_var, value=1)
ChestPainType_ATA_label = tk.Radiobutton(window, text="ATA", variable=ChestPainType_var, value=2)
ChestPainType_NAP_label = tk.Radiobutton(window, text="NAP", variable=ChestPainType_var, value=3)
ChestPainType_TA_label = tk.Radiobutton(window, text="TA", variable=ChestPainType_var, value=4)

#Resting ECG toggle switch
RestingECG_var=tk.IntVar()
RestingECG_LVH_label = tk.Radiobutton(window, text="LVH", variable=RestingECG_var, value=1)
RestingECG_Normal_label = tk.Radiobutton(window, text="Normal", variable=RestingECG_var, value=2)
RestingECG_ST_label = tk.Radiobutton(window, text="ST", variable=RestingECG_var, value=3)

#Exercise angina switch
ExerciseAngina_var = tk.IntVar()
ExerciseAngina_N_label = tk.Radiobutton(window, text="N", variable=ExerciseAngina_var, value=1)
ExerciseAngina_Y_label = tk.Radiobutton(window, text="Y", variable=ExerciseAngina_var, value=2)

#ST Slope curve
ST_Slope_var = tk.IntVar()
ST_Slope_Down_label = tk.Radiobutton(window, text="Down", variable=ST_Slope_var, value=1)
ST_Slope_Flat_label = tk.Radiobutton(window, text="Flat", variable=ST_Slope_var, value=2)
ST_Slope_Up_label = tk.Radiobutton(window, text="UP", variable=ST_Slope_var, value=3)



# Calculate button
calculate_button = tk.Button(window, text="Calculate Metrics", command=calculate_metrics)

# Display results
result_label = tk.Label(window, text="", font=("Arial", 12))

# Place widgets on the screen
Age_label.grid(row=0, column=0, padx=10, pady=5)
Age.grid(row=0, column=1, padx=10, pady=5)
Cholesterol_label.grid(row=1, column=0, padx=10, pady=5)
Cholesterol.grid(row=1, column=1, padx=10, pady=5)
MaxHR_label.grid(row=2, column=0, padx=10, pady=5)
MaxHR.grid(row=2, column=1, padx=10, pady=5)
Gender_label.grid(row=3, column=0, padx=10, pady=5)
Sex_M_label.grid(row=3, column=1, padx=10, pady=5)
Sex_F_label.grid(row=3, column=2, padx=10, pady=5)



calculate_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
result_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()