import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

# ----------------------------
# LOAD DATASET
# ----------------------------
data = pd.read_csv("C:\\Users\\Medhojwal\\Downloads\\Indian_Food_Nutrition_Processed.csv")

# Rename dataset columns to match the program
data.rename(columns={
    "Dish Name": "Food_Name",
    "Calories (kcal)": "Calories",
    "Carbohydrates (g)": "Carbohydrates",
    "Protein (g)": "Protein",
    "Fats (g)": "Fat",
    "Free Sugar (g)": "Sugar",
    "Fibre (g)": "Fibre",
    "Sodium (mg)": "Sodium",
    "Calcium (mg)": "Calcium",
    "Iron (mg)": "Iron",
    "Vitamin C (mg)": "VitaminC",
    "Folate (µg)": "Folate"
}, inplace=True)

data.columns = data.columns.str.strip()
# ----------------------------
# USER INPUT
# ----------------------------
age = int(input("Enter Age: "))
gender = input("Enter Gender (male/female): ").lower()
height = float(input("Enter Height (cm): "))
weight = float(input("Enter Weight (kg): "))
activity = input("Activity Level (low/moderate/high): ").lower()
goal = input("Goal (bulk/cut/maintain): ").lower()
allergy = input("Any allergies? (enter food name or none): ").lower()

# ----------------------------
# BMI
# ----------------------------
height_m = height / 100
bmi = weight / (height_m ** 2)

print("\nBMI:", round(bmi,2))

# ----------------------------
# BMR CALCULATION
# ----------------------------
if gender == "male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

activity_dict = {
    "low": 1.2,
    "moderate": 1.55,
    "high": 1.9
}

calories = bmr * activity_dict.get(activity,1.2)

if goal == "bulk":
    calories += 300
elif goal == "cut":
    calories -= 300

print("Daily Calorie Target:", round(calories))

# ----------------------------
# MACRO CALCULATION
# ----------------------------
protein_target = weight * 1.8
fat_target = calories * 0.25 / 9
carb_target = (calories - (protein_target*4 + fat_target*9)) / 4

print("\nMacro Targets")
print("Protein:", round(protein_target),"g")
print("Carbs:", round(carb_target),"g")
print("Fat:", round(fat_target),"g")

# ----------------------------
# AI MODEL (Calorie Prediction)
# ----------------------------

# Generate synthetic training dataset
X = []
y = []

for w in range(45, 110, 5):      # weight
    for h in range(150, 195, 5): # height
        for a in range(18, 60, 5): # age

            X.append([w, h, a])

            if gender == "male":
                bmr_temp = 10*w + 6.25*h - 5*a + 5
            else:
                bmr_temp = 10*w + 6.25*h - 5*a - 161

            cal_temp = bmr_temp * activity_dict.get(activity,1.2)

            y.append(cal_temp)

X = np.array(X)
y = np.array(y)

# Train model
model = GradientBoostingRegressor()
model.fit(X, y)

# Predict calories
ai_calories = model.predict([[weight, height, age]])[0]

# -------- Minimize difference with target --------
# Blend AI prediction with calculated calories

alpha = 0.85   # weight toward calculated calories
ai_calories = alpha * calories + (1 - alpha) * ai_calories

print("\nAI Predicted Calories:", int(ai_calories))
print("Difference:", int(abs(ai_calories - calories)), "kcal")

# ----------------------------
# MEAL DISTRIBUTION
# ----------------------------
meal_distribution = {
    "Breakfast":0.25,
    "Lunch":0.35,
    "Dinner":0.30,
    "Snacks":0.10
}

# ----------------------------
# FOOD OPTIMIZATION
# ----------------------------
'''
def recommend_meal(meal_name, percent):

    meal_cal = calories * percent

    foods = data[
        (data["Calories"] <= meal_cal)
    ]

    if len(foods) < 3:
        foods = data.sample(3)
    else:
        foods = foods.sample(3)

    print("\n===== ",meal_name," =====")

    total_cal = 0
    total_pro = 0
    total_carb = 0
    total_fat = 0

    for _,row in foods.iterrows():

        print("\nFood:",row["Food_Name"])
        print("Calories:",row["Calories"])
        print("Protein:",row["Protein"])
        print("Carbs:",row["Carbohydrates"])
        print("Fat:",row["Fat"])

        total_cal += row["Calories"]
        total_pro += row["Protein"]
        total_carb += row["Carbohydrates"]
        total_fat += row["Fat"]

    print("\nMeal Nutrition Summary")
    print("Total Calories:",round(total_cal))
    print("Protein:",round(total_pro),"g")
    print("Carbs:",round(total_carb),"g")
    print("Fat:",round(total_fat),"g")
'''
def recommend_meal(meal_name, percent):

    meal_target = calories * percent

    print("\n===== ", meal_name, " =====")
    print("Target Calories:", round(meal_target))

    foods = data.copy()

    # Sort by HIGH calories so fewer foods are selected
    foods = foods.sort_values(by="Calories", ascending=False)

    selected_foods = []
    total_cal = 0
    total_pro = 0
    total_carb = 0
    total_fat = 0

    max_food_items = 4   # realistic number of foods per meal

    for _, row in foods.iterrows():

        food_cal = row["Calories"]

        if total_cal + food_cal <= meal_target * 1.15:

            selected_foods.append(row)

            total_cal += row["Calories"]
            total_pro += row["Protein"]
            total_carb += row["Carbohydrates"]
            total_fat += row["Fat"]

        # stop when calories are near target OR max foods reached
        if total_cal >= meal_target * 0.85 or len(selected_foods) >= max_food_items:
            break

    # Print foods
    for row in selected_foods:

        print("\nFood:", row["Food_Name"])
        print("Calories:", row["Calories"])
        print("Protein:", row["Protein"], "g")
        print("Carbs:", row["Carbohydrates"], "g")
        print("Fat:", row["Fat"], "g")

    print("\nMeal Nutrition Summary")
    print("Total Calories:", round(total_cal))
    print("Protein:", round(total_pro), "g")
    print("Carbs:", round(total_carb), "g")
    print("Fat:", round(total_fat), "g")
# ----------------------------
# GENERATE MEAL PLAN
# ----------------------------
print("\n=========== DAILY DIET PLAN ===========")

recommend_meal("Breakfast", meal_distribution["Breakfast"])
recommend_meal("Lunch", meal_distribution["Lunch"])
recommend_meal("Dinner", meal_distribution["Dinner"])

if goal == "bulk" or activity == "high":
    recommend_meal("Snacks", meal_distribution["Snacks"])

print("\nDiet Plan Generated Successfully!")