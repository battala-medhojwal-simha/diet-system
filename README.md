# diet-recommendation-system

A smart **AI-powered Diet Recommendation System** that generates personalized meal plans based on a user's physical profile, fitness goals, and nutritional requirements. The system uses machine learning and nutritional data to recommend balanced Indian meals while calculating calorie and macronutrient targets.

---

## Overview

The AI-Based Diet Recommendation System is designed to assist users in achieving their health and fitness goals by generating customized diet plans.

The system:

- Calculates **BMI**, **BMR**, and **Daily Calorie Requirements**
- Determines personalized **Protein, Carbohydrate, and Fat targets**
- Recommends suitable Indian food items from a nutrition dataset
- Supports:
  - Weight Loss
  - Weight Gain (Bulk)
  - Weight Maintenance
- Considers user allergies while generating recommendations

---

## Features

- User Profile Collection
  - Age
  - Gender
  - Height
  - Weight
  - Activity Level
  - Fitness Goal
  - Allergies

- Health Calculations
  - BMI
  - Basal Metabolic Rate (BMR)
  - Total Daily Energy Expenditure (TDEE)

- Personalized Meal Recommendations

- Macronutrient Calculation
  - Protein
  - Carbohydrates
  - Fat

- Allergy-aware Recommendations

- Nutritional Analysis

---

## Machine Learning

The project uses **Gradient Boosting Regressor** from **Scikit-learn** to predict and recommend suitable foods based on nutritional requirements.

### Algorithm

- Gradient Boosting Regressor

### Future Improvements

- Random Forest
- XGBoost
- Deep Learning Models
- Reinforcement Learning

---

## Dataset

The project uses an **Indian Food Nutrition Dataset** containing nutritional information such as:

- Food Name
- Calories
- Protein
- Carbohydrates
- Fat
- Sugar
- Fibre
- Sodium
- Calcium
- Iron
- Vitamin C
- Folate

Dataset File:

```text
Indian_Food_Nutrition_Processed.csv
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- CSV Dataset

---

## Project Structure

```text
AI-Based-Diet-Recommendation-System/
│
├── aidietrecomm2.py
├── Indian_Food_Nutrition_Processed.csv
├── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/AI-Based-Diet-Recommendation-System.git
```

### Move into the project directory

```bash
cd AI-Based-Diet-Recommendation-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

```bash
python aidietrecomm2.py
```

---

## Sample Input

```text
Age: 20
Gender: Male
Height: 175 cm
Weight: 78 kg
Activity Level: Moderate
Goal: Bulk
Allergy: None
```

---

## Sample Output

```text
Enter Age: 21
Enter Gender (male/female): male
Enter Height (cm): 174
Enter Weight (kg): 75
Activity Level (low/moderate/high): moderate
Goal (bulk/cut/maintain): cut
Any allergies? (enter food name or none): none

BMI: 24.77
Daily Calorie Target: 2393

Macro Targets
Protein: 135 g
Carbs: 314 g
Fat: 66 g

AI Predicted Calories: 2438
Difference: 45 kcal

=========== DAILY DIET PLAN ===========

=====  Breakfast  =====
Target Calories: 598

Food: Boondi raita
Calories: 687.72
Protein: 2.19 g
Carbs: 3.96 g
Fat: 73.83 g

Meal Nutrition Summary
Total Calories: 688
Protein: 2 g
Carbs: 4 g
Fat: 74 g

=====  Lunch  =====
Target Calories: 838

Food: Soyabean muthias
Calories: 839.33
Protein: 2.46 g
Carbs: 3.7 g
Fat: 90.45 g

Meal Nutrition Summary
Total Calories: 839
Protein: 2 g
Carbs: 4 g
Fat: 90 g

=====  Dinner  =====
Target Calories: 718

Food: Mathri
Calories: 805.12
Protein: 1.75 g
Carbs: 12.32 g
Fat: 83.1 g

Meal Nutrition Summary
Total Calories: 805
Protein: 2 g
Carbs: 12 g
Fat: 83 g

Diet Plan Generated Successfully!
```

---

## Workflow

```text
User Input
      │
      ▼
BMI & BMR Calculation
      │
      ▼
Calorie Requirement (TDEE)
      │
      ▼
Macronutrient Calculation
      │
      ▼
Machine Learning Recommendation
      │
      ▼
Personalized Diet Plan
```

---

## Future Enhancements

- Web Application using Flask or Django
- React Frontend
- Android Application
- Disease-specific Meal Planning
- Region-wise Food Recommendation
- Meal Scheduling
- Grocery List Generation
- Nutrition Tracking Dashboard
- AI Chatbot for Dietary Guidance
- Wearable Device Integration

---

## Required Libraries

```text
pandas
numpy
scikit-learn
```

Install them using:

```bash
pip install pandas numpy scikit-learn
```

---

## Authors

- **B. Medhojwal Simha**
- **A. Sruveen**
- **B. Poornachandar**

Department of Computer Science and Engineering (AI & ML)

Joginpally B.R. Engineering College

---

## 📄 License

This project is developed for **academic and educational purposes** as part of a Bachelor of Technology Mini Project.
