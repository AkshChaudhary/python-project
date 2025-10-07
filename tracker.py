#Name: Aksh  chaudhary
#Date: 6 october 2025
#Project: Daily Tracker Project 

print("Welcome to daily tracker")
print("enter your daily calories intake")

meal_names = []
Calorie_amounts = []

num_meals = int(input("How many meals do you want to enter today?"))

for i  in range(num_meals):
    meal = input(f"Enter{i+1}th meal name")
    cal = float(input(f"Enter calories for{i+1}th meal"))
    meal_names.append(meal)
    Calorie_amounts.append(cal)

total_calories = sum(Calorie_amounts)
avg_calories = total_calories/num_meals
daily_limit = float(input("Enter your daily calorie limit"))

if total_calories > daily_limit:
    status_msg = f"Warning: You have exceeded your daily limit by {total_calories - daily_limit} calories."
else:
    status_msg = f"Great! You are within your daily limit. You have {daily_limit - total_calories} calories remaining."

print("Meal Name\tCalories")
print("-" * 30)

for meal, cal in zip(meal_names, Calorie_amounts):
    print(f"{meal}\t\t{cal}")

print(f"Total:\t\t{total_calories:}")
print(f"Average:\t{avg_calories:}")
print(status_msg)
