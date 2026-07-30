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
BMI: 25.47

Daily Calorie Target: 2860 kcal

Protein Target: 140 g
Carbohydrates Target: 390 g
Fat Target: 79 g

Recommended Foods

• Brown Rice
• Chicken Breast
• Oats
• Eggs
• Milk
• Banana
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
