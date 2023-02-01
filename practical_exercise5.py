def compute_grade(note):
    if note <= 100 and note >= 70:
        return 'A'
    elif note < 70 and note >= 50:
        return 'B'
    elif note < 50 and note >= 30:
        return 'C'
    elif note < 30 and note >= 0:
        return 'F'
    else:
        print("Wrong score entered...")

def report_message(name,score):
    letter = compute_grade(score)
    print(f"{name} scored {score} points in Chemistry and got the grade {letter}")
    
for i in range(0,2):
    student_name = input("Enter a student name: ")
    student_score = int(input("Enter a score: "))
    report_message(student_name,student_score)




zach_file = open("zach_report.txt","w")
content = zach_file.write("Hello Zach...")
zach_file.close()

import os
sophie_file = open("sophie_report.txt","r")
content = sophie_file.read()
if os.stat("sophie_report.txt").st_size == 0:
    sophie_file = open("sophie_report.txt","w")
    sophie_file.write("There is an existing report card for Sophie.")
    sophie_file.close()
else:
    print(content)
    sophie_file.close()




def student_grade(name,score):
    if score <= 100 and score >= 70:
        letter = 'A'
        print(f"{name} scored {score} points in Chemistry and got the grade {letter}")
        return name,letter
    elif score < 70 and score >= 50:
        letter = 'B'
        return name,letter
    elif score < 50 and score >= 30:
        letter = 'C'
        return name,letter
    elif score < 30 and score >= 0:
        letter = 'F'
        return name,letter
    else:
        print("Wrong score entered...")

    if name == "":
        print("Student name was missing...")

student_file = open("name_grade.txt","r")
store_file = open("grades.txt","w")
for line in student_file:
    name,score = line.split(':')
    student_grade(name,int(score))
    print(name,score,file=store_file)

student_file.close()
store_file.close()
