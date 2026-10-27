"""College Life Adventure: a small text-based semester simulation."""

def choose_course_load(gpa, study_hours, stress_level):
    print("\nChoose your course load:")
    print("A) Light (12 credits)")
    print("B) Standard (15 credits)")
    print("C) Heavy (18 credits)")
    choice = input("Your choice (A/B/C): ").strip().upper()

    if choice == "A":
        study_hours -= 10 if gpa > 3.0 else 5
        stress_level -= 20 if gpa > 3.0 else 10
    elif choice == "B":
        if gpa > 3.0:
            study_hours -= 5
            stress_level -= 10
        else:
            study_hours += 10
            stress_level += 5
    elif choice == "C":
        if gpa > 3.5:
            study_hours += 5
            stress_level += 10
        else:
            study_hours += 20
            stress_level += 10
    else:
        print("Invalid course load. Keeping the standard starting values.")
        return study_hours, stress_level

    study_hours = max(0, study_hours)
    stress_level = max(0, min(100, stress_level))
    print(f"Study hours: {study_hours} | Stress level: {stress_level}")
    return study_hours, stress_level


def choose_study_subject(gpa, stress_level, social_points):
    subjects = {
        "programming": 30,
        "math": 20,
        "english": 15,
        "history": 10,
    }
    print("\nAvailable study subjects: Programming, Math, English, History")
    subject = input("Choose a subject: ").strip().lower()

    if subject not in subjects:
        print("That subject is not available. Social points stay the same.")
        return social_points

    if gpa < 2.0 and social_points > 50:
        social_points -= 20 if subject == "programming" else 5
    elif gpa < 3.0 and social_points > 50:
        social_points -= 10 if subject == "programming" else 1
    elif gpa >= 3.5 and stress_level <= 80:
        social_points += subjects[subject]

    social_points = max(0, min(100, social_points))
    print(f"Social points: {social_points}")
    return social_points


def describe_semester(gpa, stress_level, social_points):
    print("\n=== Semester Outcome ===")
    if gpa >= 3.5 and stress_level <= 40 and social_points >= 50:
        print("Outstanding Semester: excellent academics and a healthy balance.")
    elif gpa >= 3.0 and stress_level <= 60 and social_points >= 40:
        print("Good Semester: solid academics and manageable stress.")
    elif gpa >= 2.5 and stress_level <= 80 and social_points >= 30:
        print("Average Semester: satisfactory, with room to improve your balance.")
    else:
        print("Struggling Semester: consider adjusting your workload and seeking support.")


def main():
    # Starting values make each run easy to compare.
    current_gpa = 3.2
    study_hours = 25
    social_points = 50
    stress_level = 50

    study_hours, stress_level = choose_course_load(
        current_gpa, study_hours, stress_level
    )
    social_points = choose_study_subject(current_gpa, stress_level, social_points)
    describe_semester(current_gpa, stress_level, social_points)


if __name__ == "__main__":
    main()
