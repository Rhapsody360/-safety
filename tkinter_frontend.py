import tkinter as tk
import tensorflow as tf
import pandas as pd

model = tf.keras.models.load_model('keras_model')

def calculate_metrics():
    # Get user inputs
    age = int(Age.get())
    restingBP = int(RestingBP.get())
    cholesterol = float(Cholesterol.get())
    fastingBS = int(FastingBS.get())
    max_heart_rate = int(MaxHR.get())
    oldpeak=float(Oldpeak.get())
    gender = int(gender_var.get())
    chestPainType = int(ChestPainType_var.get())
    resting_ECG = int(RestingECG_var.get())
    exerciseAngina = int(ExerciseAngina_var.get())
    sT_Slope = int(ST_Slope_var.get())

    #correct the categorical variables
    #gender
    if (gender==1):
        Sex_M,Sex_F=1,0
    else :
        Sex_M,Sex_F=0,1

    #chesptpaintype
    if (chestPainType == 1):
        ChestPainType_ASY,ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA = 1,0,0,0
    elif (chestPainType == 2):
        ChestPainType_ASY,ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA = 0,1,0,0
    elif (chestPainType == 3):
        ChestPainType_ASY,ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA = 0,0,1,0
    else:
        ChestPainType_ASY,ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA = 0,0,0,1

    #resting ecg
    if (resting_ECG == 1):
        RestingECG_LVH,RestingECG_Normal,RestingECG_ST = 1,0,0
    elif (resting_ECG == 2):
        RestingECG_LVH,RestingECG_Normal,RestingECG_ST = 0,1,0
    elif (resting_ECG == 3):
        RestingECG_LVH,RestingECG_Normal,RestingECG_ST = 0,0,1

    #exercise
    if (exerciseAngina==1):
        ExerciseAngina_N,ExerciseAngina_Y = 1,0
    else:
        ExerciseAngina_N,ExerciseAngina_Y = 0,1
    #st slope
    if (sT_Slope == 1):
        ST_Slope_Down,ST_Slope_Flat,ST_Slope_Up = 1,0,0
    if (sT_Slope == 2):
        ST_Slope_Down,ST_Slope_Flat,ST_Slope_Up = 0,1,0
    if (sT_Slope == 3):
        ST_Slope_Down,ST_Slope_Flat,ST_Slope_Up = 0,0,1
    

    # Calculate health metrics: use your neural network to predict the OP heart risk number
    new_patient = pd.DataFrame({"Age":[age],
                                "RestingBP":[restingBP],
                                "Cholesterol":[cholesterol],
                                "FastingBS":[fastingBS],
                                "MaxHR":[max_heart_rate],
                                "Oldpeak":[oldpeak],
                                "Sex_F":[Sex_F],
                                "Sex_M":[Sex_M],
                                "ChestPainType_ASY":[ChestPainType_ASY],
                                "ChestPainType_ATA":[ChestPainType_ATA],
                                "ChestPainType_NAP":[ChestPainType_NAP],
                                "ChestPainType_TA":[ChestPainType_TA],
                                "RestingECG_LVH":[RestingECG_LVH],
                                "RestingECG_Normal":[RestingECG_Normal],
                                "RestingECG_ST":[RestingECG_ST],
                                "ExerciseAngina_N":[ExerciseAngina_N],
                                "ExerciseAngina_Y":[ExerciseAngina_Y],
                                "ST_Slope_Down":[ST_Slope_Down],
                                "ST_Slope_Flat":[ST_Slope_Flat],
                                "ST_Slope_Up":[ST_Slope_Up]})    
    op=float(model.predict(new_patient))
    # Example: Calculate risk factors based on age, cholesterol, and heart rate

    # Display the results (you can customize this part)
    result_label.config(text= f"Age: {age} years\n"
                              f"restingBP: {restingBP}\n"
                              f"Cholesterol: {cholesterol} mg/dL\n"
                              f"Gender: {'Male' if gender == 1 else 'Female'}\n"
                              f"FastingBS: {fastingBS}\n"
                              f"Max Heart Rate: {max_heart_rate} bpm\n"
                              f"oldpeak:{oldpeak}\n"
                              f"Chestpaintype:{chestPainType}\n"
                              f"resting ecg:{resting_ECG}\n"
                              f"exercise:{exerciseAngina}\n"
                              f"st slope:{sT_Slope}\n"
                              f"!!! PREDICTED OP:{op*100} % RISK !!!\n"
    )
    

# Create the main window
window = tk.Tk()
window.title("Health Metrics Calculator")
# window.geometry("400x300")

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
RestingBP_label.grid(row=1,column = 0)
RestingBP.grid(row=1,column=1)
Cholesterol_label.grid(row=2, column=0, padx=10, pady=5)
Cholesterol.grid(row=2, column=1, padx=10, pady=5)
FastingBS_label.grid(row = 3,column=0)
FastingBS.grid(row = 3,column = 1)
MaxHR_label.grid(row=4, column=0, padx=10, pady=5)
MaxHR.grid(row=4, column=1, padx=10, pady=5)
Oldpeak_label.grid(row = 5,column=0)
Oldpeak.grid(row =5,column=1)
Gender_label.grid(row=6, column=0, padx=10, pady=5)
Sex_M_label.grid(row=6, column=1, padx=10, pady=5)
Sex_F_label.grid(row=6, column=2, padx=10, pady=5)
ChestPainType_label.grid(row = 7,column =0)
ChestPainType_ASY_label.grid(row=7,column=1)
ChestPainType_ATA_label.grid(row=7,column=2)
ChestPainType_NAP_label.grid(row=7,column=3)
ChestPainType_TA_label.grid(row=7,column =4)
RestingECG_label.grid(row = 8,column=0)
RestingECG_LVH_label.grid(row =8,column=1)
RestingECG_Normal_label.grid(row = 8,column=2)
RestingECG_ST_label.grid(row=8,column=3)
ExerciseAngina_label.grid(row = 9,column=0)
ExerciseAngina_N_label.grid(row = 9,column = 1)
ExerciseAngina_Y_label.grid(row = 9,column=2)
ST_Slope_label.grid(row=10,column=0)
ST_Slope_Down_label.grid(row = 10, column = 1)
ST_Slope_Flat_label.grid(row = 10,column =2)
ST_Slope_Up_label.grid(row=10,column=3)




calculate_button.grid(row=11, column=0, columnspan=3, padx=10, pady=10)
result_label.grid(row=12, column=0, columnspan=3, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()