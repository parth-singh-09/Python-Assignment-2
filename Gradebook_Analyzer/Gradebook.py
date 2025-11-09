# =========================================================
# Project: GradeBook_Analyzer 
# Name: Parth Singh 
# Roll No: 2501730144
# Description:
#   CLI tool to input or import student marks,
#   calculate statistics, assign grades, and print summaries.
# =========================================================

import csv

# ------------------- STATISTICAL FUNCTIONS -------------------

def calculate_average(student_scores):
    """Calculate average marks."""
    total_marks = sum(student_scores.values())
    total_students = len(student_scores)
    return total_marks / total_students if total_students > 0 else 0


def calculate_median(student_scores):
    """Calculate median marks."""
    sorted_scores = sorted(student_scores.values())
    count = len(sorted_scores)
    if count == 0:
        return 0
    mid_index = count // 2
    if count % 2 == 0:
        return (sorted_scores[mid_index - 1] + sorted_scores[mid_index]) / 2
    else:
        return sorted_scores[mid_index]


def find_highest_score(student_scores):
    """Return the highest marks."""
    return max(student_scores.values()) if student_scores else None


def find_lowest_score(student_scores):
    """Return the lowest marks."""
    return min(student_scores.values()) if student_scores else None


def assign_letter_grades(student_scores):
    """Assign grades based on marks."""
    grade_book = {}
    for student_name, score in student_scores.items():
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grade_book[student_name] = grade
    return grade_book


def count_grade_distribution(grade_book):
    """Count number of students per grade."""
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grade_book.values():
        distribution[grade] += 1
    return distribution


# ------------------- PASS/FAIL FILTER -------------------

def separate_pass_fail(student_scores):
    """Separate passed and failed students."""
    passed_students = [name for name, score in student_scores.items() if score >= 40]
    failed_students = [name for name, score in student_scores.items() if score < 40]
    return passed_students, failed_students


# ------------------- CSV LOAD FUNCTION -------------------

def import_from_csv(file_path):
    """Load student marks from a CSV file."""
    student_scores = {}
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)  # Skip header if present
            for row in csv_reader:
                if len(row) == 2:
                    student_name = row[0].strip()
                    try:
                        student_scores[student_name] = float(row[1])
                    except ValueError:
                        print(f"Invalid mark for {student_name}. Skipping.")
        if not student_scores:
            print("No valid records found in file.")
        else:
            print(f"\n✅ Successfully loaded {len(student_scores)} records from '{file_path}'.")
    except FileNotFoundError:
        print("❌ File not found. Please check the file name.")
    return student_scores


# ------------------- DISPLAY FUNCTION -------------------

def show_table(student_scores, grade_book):
    """Display results in tabular form."""
    print("\n" + "-" * 50)
    print(f"{'Name':<20}{'Marks':<10}{'Grade':<10}")
    print("-" * 50)
    for name, score in student_scores.items():
        print(f"{name:<20}{score:<10.1f}{grade_book[name]:<10}")
    print("-" * 50)


# ------------------- MAIN PROGRAM -------------------

def main():
    print("===== GRADEBOOK ANALYZER =====")

    while True:
        print("\n1. Enter Marks Manually")
        print("2. Import Marks from CSV File")
        print("3. Exit Program")
        user_choice = input("Enter your choice (1-3): ")

        student_scores = {}

        if user_choice == '1':
            num_students = int(input("\nEnter number of students: "))
            for i in range(num_students):
                student_name = input(f"Enter name of student {i + 1}: ")
                score = float(input(f"Enter marks of {student_name}: "))
                student_scores[student_name] = score

        elif user_choice == '2':
            file_path = input("\nEnter CSV filename (with .csv extension): ")
            student_scores = import_from_csv(file_path)

        elif user_choice == '3':
            print("\nExiting GradeBook Analyzer. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
            continue

        if not student_scores:
            continue

        # ---- Perform Analysis ----
        avg_marks = calculate_average(student_scores)
        median_marks = calculate_median(student_scores)
        top_score = find_highest_score(student_scores)
        low_score = find_lowest_score(student_scores)
        grade_book = assign_letter_grades(student_scores)
        grade_distribution = count_grade_distribution(grade_book)
        passed_students, failed_students = separate_pass_fail(student_scores)

        # ---- Display Results ----
        show_table(student_scores, grade_book)

        print("\n STATISTICAL SUMMARY:")
        print(f"Average Marks: {avg_marks:.2f}")
        print(f"Median Marks: {median_marks:.2f}")
        print(f"Highest Marks: {top_score}")
        print(f"Lowest Marks: {low_score}")

        print("\n GRADE DISTRIBUTION:")
        for grade, count in grade_distribution.items():
            print(f"{grade}: {count}")

        print("\n PASS/FAIL SUMMARY:")
        print(f"Passed ({len(passed_students)}): {', '.join(passed_students) if passed_students else 'None'}")
        print(f"Failed ({len(failed_students)}): {', '.join(failed_students) if failed_students else 'None'}")


# ------------------- ENTRY POINT -------------------

if __name__ == "__main__":
    main()
