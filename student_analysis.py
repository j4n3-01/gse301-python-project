# PART 1: DATA COLLECTION AND STORAGE

# Variable Declaration and Data Types
student_name = "Amina Yusuf"
matric_number = "23/60AC001"
age = 21
cgpa = 4.25
is_active = True
courses_registered = ["Python", "Statistics", "Data Science", "AI"]
grades = {
    "Python": "A",
    "Statistics": "B",
    "Data Science": "A",
    "AI": "A"
}

# Data Structures in Action
# List of student names
student_names = [
    "Rasheed Fatia",
    "Yusuf Adeoye",
    "Moses Oyedele",
    "Timi Abidoye",
    "Nimah Nina"
]

# Dictionary for each student's full profile
students = [
    {
        "name": "Rasheed Fatia",
        "matric": "23/60AC389",
        "age": 21,
        "cgpa": 4.81,
        "courses": ["ELE567", "Data Science", "Statistics"],
        "grades": {"ELE567": "A", "Data Science": "A", "Statistics": "A"},
        "is_active": True,
        "outstanding_courses": 0
    },
    {
        "name": "Yusuf Adeoye",
        "matric": "23/70JC093",
        "age": 22,
        "cgpa": 3.45,
        "courses": ["Python", "AI"],
        "grades": {"Python": "B", "AI": "A"},
        "is_active": True,
        "outstanding_courses": 0
    },
    {
        "name": "Moses Oyedele",
        "matric": "23/80DC045",
        "age": 20,
        "cgpa": 4.20,
        "courses": ["Data Science", "Statistics", "Python"],
        "grades": {"Data Science": "A", "Statistics": "A", "Python": "B"},
        "is_active": True,
        "outstanding_courses": 0
    },
    {
        "name": "Timi Abidoye",
        "matric": "23/90EC012",
        "age": 23,
        "cgpa": 2.90,
        "courses": ["Python", "Statistics"],
        "grades": {"Python": "C", "Statistics": "C"},
        "is_active": False,
        "outstanding_courses": 1
    },
    {
        "name": "Nimah Nina",
        "matric": "23/50BC078",
        "age": 21,
        "cgpa": 3.95,
        "courses": ["AI", "Data Science", "Python"],
        "grades": {"AI": "B", "Data Science": "A", "Python": "A"},
        "is_active": True,
        "outstanding_courses": 0
    }
]

# Set to store unique courses offered in the department
unique_courses = set()
for student in students:
    unique_courses.update(student["courses"])

# Tuple for fixed department information
department_info = ("Computer Science Department", "Faculty of Technology", 2025)

# PART 2: DATA PROCESSING AND LOGIC

# Conditional Statements for Grading
def calculate_grade(score):
    """
    Accepts a score from 0 to 100 and returns a grade
    Uses IF, ELIF, ELSE for grading and MATCH CASE for feedback
    """
    # Validate score range
    if score < 0 or score > 100:
        return "Invalid", "Score must be between 0 and 100"
    
    # Determine grade using IF, ELIF, ELSE
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"
    
    # Use MATCH CASE to print feedback based on grade
    match grade:
        case "A":
            feedback = "Excellent performance! Outstanding work!"
        case "B":
            feedback = "Very good job! Keep it up!"
        case "C":
            feedback = "Good effort. You can do better."
        case "D":
            feedback = "You passed, but there's room for improvement."
        case "E":
            feedback = "Needs significant improvement."
        case "F":
            feedback = "Failed. Please work harder next time."
        case _:
            feedback = "Unknown grade"
    
    return grade, feedback


#Type Conversion and Validation
def validate_student_input():
    
    try:
        # Get input as strings
        age_str = input("Enter age: ")
        cgpa_str = input("Enter CGPA: ")
        
        # Convert to appropriate types
        age = int(age_str)
        cgpa = float(cgpa_str)
        
        # Validate age between 16 and 40
        if not (16 <= age <= 40):
            raise ValueError("Age must be between 16 and 40")
        
        # Validate CGPA between 0.0 and 5.0
        if not (0.0 <= cgpa <= 5.0):
            raise ValueError("CGPA must be between 0.0 and 5.0")
        
        print("Valid input!")
        print(f"Age: {age}")
        print(f"CGPA: {cgpa}")
        return age, cgpa
        
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None, None



# PART 3: ANALYSIS AND REPORTING

#List Operations and Slicing
def demonstrate_list_operations():
    """
    Demonstrate various list slicing operations
    """
    assignment_scores = [65, 78, 90, 88, 72, 60, 95, 85, 70, 80]
    
    # Extract top 3 scores using slicing
    sorted_scores = sorted(assignment_scores, reverse=True)
    top_3_scores = sorted_scores[:3]
    
    # Extract last 5 scores using negative indexing
    last_5_scores = assignment_scores[-5:]
    
    # Extract every other score using step slicing
    every_other_score = assignment_scores[::2]
    
    print("\nLIST OPERATIONS AND SLICING")
    print("-" * 50)
    print(f"Original scores: {assignment_scores}")
    print(f"Top 3 scores: {top_3_scores}")
    print(f"Last 5 scores: {last_5_scores}")
    print(f"Every other score: {every_other_score}")
    
    return top_3_scores, last_5_scores, every_other_score

#Set Operations
def demonstrate_set_operations():
    """
    Demonstrating set operations: intersection, union, difference
    """
    # Students who passed Python
    set_pass = {"Rasheed Fatia", "Yusuf Adeoye", "Moses Oyedele", "Nimah Nina"}
    
    # Students with CGPA above 4.0
    set_merit = {"Rasheed Fatia", "Moses Oyedele", "Timi Abidoye"}
    
    # Finding students who passed and have merit (intersection)
    passed_and_merit = set_pass & set_merit
    
    # All distinct students in both sets (union)
    all_students = set_pass | set_merit
    
    # Students who passed but do not have merit (difference)
    passed_no_merit = set_pass - set_merit
    
    print("\nSET OPERATIONS")
    print("-" * 50)
    print(f"Students who passed Python: {set_pass}")
    print(f"Students with CGPA above 4.0: {set_merit}")
    print(f"Passed AND have merit (intersection): {passed_and_merit}")
    print(f"All distinct students (union): {all_students}")
    print(f"Passed but NO merit (difference): {passed_no_merit}")
    
    return passed_and_merit, all_students, passed_no_merit

# PART 4: INTERACTIVE MENU SYSTEM

#Eligibility Checker (defined before menu so as to use it)
def check_graduation_eligibility(student):
    """
    Uses logical operators (and, or) to determine graduation eligibility
    Returns True or False and a detailed message
    """
    # Check eligibility criteria
    cgpa_ok = student["cgpa"] >= 2.5
    no_outstanding = student["outstanding_courses"] == 0
    is_active = student["is_active"]
    
    # Determine eligibility using AND operator
    is_eligible = cgpa_ok and no_outstanding and is_active
    
    # Build detailed message
    print(f"\nChecking eligibility...")
    print(f"Matric Number: {student['matric']}")
    print(f"CGPA: {student['cgpa']}")
    print(f"Outstanding Courses: {student['outstanding_courses']}")
    print(f"Active Status: {student['is_active']}")
    print("\nEligibility Result:")
    
    if is_eligible:
        message = f"{student['name']} is eligible for graduation."
        return True, message
    else:
        # Build list of reasons for ineligibility
        reasons = []
        if not cgpa_ok:
            reasons.append("CGPA is below 2.5")
        if not no_outstanding:
            reasons.append(f"Has {student['outstanding_courses']} outstanding course(s)")
        if not is_active:
            reasons.append("Student is not active")
        
        message = f"{student['name']} is NOT eligible for graduation.\nReasons: {', '.join(reasons)}"
        return False, message


def find_top_performer():
    """
    Find the student with the highest CGPA
    """
    top_student = max(students, key=lambda x: x["cgpa"])
    
    print("\nTop Performer:")
    print(f"Name: {top_student['name']}")
    print(f"Matric: {top_student['matric']}")
    print(f"CGPA: {top_student['cgpa']}")
    print(f"Courses: {top_student['courses']}")


def view_all_students():
    """
    Display all students in the system
    """
    print("\nList of Students:")
    for idx, student in enumerate(students, 1):
        print(f"{idx}. {student['name']}")


def add_new_student():
    """
    Add a new student to the system with validation
    """
    print("\nAdd New Student")
    
    try:
        name = input("Enter name: ")
        matric = input("Enter matric number: ")
        age_str = input("Enter age: ")
        cgpa_str = input("Enter CGPA: ")
        
        # Type conversion
        age = int(age_str)
        cgpa = float(cgpa_str)
        
        # Validation
        if not (16 <= age <= 40):
            print("Error: Age must be between 16 and 40")
            return
        if not (0.0 <= cgpa <= 5.0):
            print("Error: CGPA must be between 0.0 and 5.0")
            return
        
        is_active_input = input("Is the student active (yes/no): ").lower()
        is_active = is_active_input == "yes"
        
        courses_input = input("Enter courses (comma separated): ")
        courses = [course.strip() for course in courses_input.split(",")]
        
        # Creating new student dictionary
        new_student = {
            "name": name,
            "matric": matric,
            "age": age,
            "cgpa": cgpa,
            "courses": courses,
            "grades": {},
            "is_active": is_active,
            "outstanding_courses": 0
        }
        
        # Adding to students list
        students.append(new_student)
        student_names.append(name)
        unique_courses.update(courses)
        
        print("\nStudent record added successfully.")
        
    except ValueError as e:
        print(f"Error: Invalid input - {e}")


# Building a Console Menu
def interactive_menu():
    """
    Create an interactive menu using MATCH CASE
    Menu repeats until user selects Exit
    """
    print("\n" + "=" * 50)
    print("Student Academic Performance System")
    print("=" * 50)
    print(f"\nLoading student records...")
    print(f"{len(students)} student profiles loaded successfully.")
    
    while True:
        print("\n" + "-" * 50)
        print("Menu Options")
        print("1. View all students")
        print("2. Add new student")
        print("3. Check eligibility for graduation")
        print("4. Find top performer")
        print("5. Exit")
        print("-" * 50)
        
        choice = input("Enter your choice: ")
        
        # Using MATCH CASE for menu options
        match choice:
            case "1":
                view_all_students()
            
            case "2":
                add_new_student()
            
            case "3":
                student_name = input("Enter student name: ")
                found = False
                for student in students:
                    if student["name"].lower() == student_name.lower():
                        result, message = check_graduation_eligibility(student)
                        print(message)
                        found = True
                        break
                if not found:
                    print(f"Student '{student_name}' not found in the system.")
            
            case "4":
                find_top_performer()
            
            case "5":
                print("\nExiting the system...")
                print("Goodbye!")
                break
            
            case _:
                print("Invalid option. Please enter a number between 1 and 5.")

# PART 5: ADVANCED CHALLENGES (OPTIONAL)

#Nested Data Processing
def process_nested_data():
    """
    Calculate average scores and identify high performers
    """
    students_scores = {
        "Rasheed Fatia": {"Python": 85, "Statistics": 90, "Data Science": 88},
        "Yusuf Adeoye": {"Python": 75, "AI": 80, "Statistics": 72},
        "Moses Oyedele": {"Python": 88, "Statistics": 85, "Data Science": 90},
        "Timi Abidoye": {"Python": 65, "Statistics": 60, "AI": 55},
        "Nimah Nina": {"Python": 80, "AI": 75, "Data Science": 85}
    }
    
    print("\nNESTED DATA PROCESSING")
    print("-" * 50)
    
    # Calculate average score for each student
    print("\nAverage Scores:")
    for name, scores in students_scores.items():
        avg_score = sum(scores.values()) / len(scores)
        print(f"{name}: {avg_score:.2f}")
    
    # Identify students who scored above 70 in all registered courses
    print("\nStudents scoring above 70 in ALL courses:")
    high_performers = [
        name for name, scores in students_scores.items()
        if all(score > 70 for score in scores.values())
    ]
    for performer in high_performers:
        print(f"- {performer}")


#Pattern Matching with MATCH CASE
def identify_data_type(value):
    """
    Uses MATCH CASE to identify the type of input
    Returns a formatted summary depending on data type
    """
    match value:
        case int():
            return f"Data Type: Integer | Value: {value} | Even: {value % 2 == 0}"
        case float():
            return f"Data Type: Float | Value: {value} | Rounded: {round(value, 2)}"
        case list():
            return f"Data Type: List | Length: {len(value)} | Items: {value}"
        case dict():
            return f"Data Type: Dictionary | Keys: {len(value)} | Keys: {list(value.keys())}"
        case str():
            return f"Data Type: String | Length: {len(value)} | Content: '{value}'"
        case set():
            return f"Data Type: Set | Size: {len(value)} | Elements: {value}"
        case tuple():
            return f"Data Type: Tuple | Length: {len(value)} | Items: {value}"
        case bool():
            return f"Data Type: Boolean | Value: {value}"
        case _:
            return f"Data Type: Unknown | Type: {type(value).__name__}"


def demonstrate_pattern_matching():
    """
    Demonstrate pattern matching with various data types
    """
    print("\nPATTERN MATCHING DEMONSTRATION")
    print("-" * 50)
    
    test_values = [
        42,
        3.14159,
        [1, 2, 3, 4, 5],
        {"name": "John", "age": 25},
        "Hello World",
        {1, 2, 3, 4, 5},
        (10, 20, 30),
        True
    ]
    
    for value in test_values:
        result = identify_data_type(value)
        print(result)


# MAIN EXECUTION

def main():
    """
    Main function to run the entire system
    """
    # Start interactive menu directly as per project requirements
    interactive_menu()


# Run the program
if __name__ == "__main__":
    main()