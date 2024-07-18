def cal_high_in_maths(student_list):
    highest_maths = 0
    high_maths_score = ""
    for student in student_list:
        if (student.get("Maths") > highest_maths):
            highest_maths = student.get("Maths")
            high_maths_score = student.get('name')
    print(f"highest in maths {high_maths_score}")

def cal_high_in_science(student_list):
    highest_science = 0
    high_science_score = ""
    for student in student_list:
        if (student.get("Science") > highest_science):
            highest_science = student.get("Science")
            high_science_score = student.get('name')
    print(f"highest in Science {high_science_score}")

def cal_high_in_social(student_list):
    highest_social = 0
    high_social_score = ""
    for student in student_list:
        if (student.get("Social") > highest_social):
            highest_maths = student.get("Social")
            high_social_score = student.get('name')
    print(f"highest in Social {high_social_score}")

student1 = {
    "Maths":78,
    "Science":56,
    "Social":90,
    "name": "Abhi"
}
student2 = {
    "Maths":58,
    "Science":96,
    "Social":70,
    "name": "vignesh"
}
student3 = {
    "Maths":48,
    "Science":56,
    "Social":100,
    "name": "Royson"
}

student_list = [student1, student2, student3]
cal_high_in_maths(student_list)
cal_high_in_science(student_list)
cal_high_in_social(student_list)
