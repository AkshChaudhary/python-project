# """
# ----------------------------------------------------
# Title   : Gradebook Analyzer
# Author  : Aksh Chaudhary
# Date    : 28 Oct 2025
# ----------------------------------------------------

import csv
import statistics

def print_menu():
    print("\n====== Gradebook Analyzer ======")
    print("1. Enter student marks manually")
    print("2. Load student marks from CSV file")
    print("3. Exit")
    print("=================================")

def load_csv(file_name):
    marks = {}
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header if present
            for row in reader:
                if len(row) >= 2:
                    name, mark = row[0], row[1]
                    marks[name] = float(mark)
        print(f"\n✅ Loaded {len(marks)} records from '{file_name}'")
    except FileNotFoundError:
        print("❌ File not found. Please check the name and try again.")
    except Exception as e:
        print("❌ Error loading CSV:", e)
    return marks

def manual_entry():
    marks = {}
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        try:
            score = float(input(f"Enter marks for {name}: "))
            marks[name] = score
        except ValueError:
            print("⚠ Invalid input. Please enter a number for marks.")
    return marks

# --- Task 3: Statistical Functions ---
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict) if marks_dict else 0

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values()) if marks_dict else 0

def find_max_score(marks_dict):
    return max(marks_dict.values()) if marks_dict else 0

def find_min_score(marks_dict):
    return min(marks_dict.values()) if marks_dict else 0

# --- Task 4: Grade Assignment ---
def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades

def grade_distribution(grades_dict):
    distribution = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for grade in grades_dict.values():
        if grade in distribution:
            distribution[grade] += 1
    return distribution

# --- Task 5: Pass/Fail Filter ---
def pass_fail_lists(marks_dict):
    passed_students = [name for name, mark in marks_dict.items() if mark >= 40]
    failed_students = [name for name, mark in marks_dict.items() if mark < 40]
    return passed_students, failed_students

# --- Task 6: Display Table ---
def display_results(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("---------------------------------")
    for name in marks:
        print(f"{name:<15}{marks[name]:<10}{grades[name]}")
    print("---------------------------------")

# --- Main Program Loop ---
def main():
    print("\n🎓 Welcome to the Gradebook Analyzer 🎓")

    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            marks = manual_entry()
        elif choice == "2":
            file_name = input("Enter CSV file name (with .csv): ").strip()
            marks = load_csv(file_name)
        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please try again.")
            continue

        if not marks:
            print("⚠ No student data to analyze.")
            continue

        # --- Perform analysis ---
        avg = calculate_average(marks)
        med = calculate_median(marks)
        high = find_max_score(marks)
        low = find_min_score(marks)
        grades = assign_grades(marks)
        dist = grade_distribution(grades)
        passed, failed = pass_fail_lists(marks)

        # --- Display results ---
        display_results(marks, grades)
        print(f"\n📊 Statistics:")
        print(f"Average: {avg:.2f}")
        print(f"Median : {med:.2f}")
        print(f"Highest: {high}")
        print(f"Lowest : {low}")

        print("\n📈 Grade Distribution:")
        for g, count in dist.items():
            print(f"  {g}: {count} student(s)")

        print(f"\n✅ Passed ({len(passed)}): {', '.join(passed) if passed else 'None'}")
        print(f"❌ Failed ({len(failed)}): {', '.join(failed) if failed else 'None'}")

        again = input("\nWould you like to analyze another dataset? (y/n): ").lower()
        if again != 'y':
            print("👋 Thank you for using Gradebook Analyzer!")
            break


if __name__ == "__main__":
    main()