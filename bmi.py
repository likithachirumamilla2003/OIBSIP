# Get user input for height and weight
height_cm = float(input("Enter your height in centimeters: "))
weight_kg = float(input("Enter your weight in kilograms: "))

# Calculate BMI
height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

# Categorize BMI and print results
if bmi <= 16:
    category = "Severe Thinness"
elif 16 < bmi <= 17:
    category = "Mild Thinness"
elif 17 < bmi <= 18.5:
    category = "Moderate Thinness"
elif 18.5 < bmi <= 25:
    category = "Normal"
elif 25 < bmi <= 30:
    category = "Overweight"
elif 30 < bmi <= 35:
    category = "Obese Class I"
elif 35 < bmi <= 40:
    category = "Obese Class II"
else:
    category = "Obese Class III"

print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")

