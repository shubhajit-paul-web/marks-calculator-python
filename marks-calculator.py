# Subjects = Bengali, English, Sanskrit, History, Computer Application
# Created by = Shubhajit Paul

print("---------------------------------------------")
print("            Exam Result Calculator           ")
print("---------------------------------------------")
Examiner_Name = input("Enter student name: ")
Examiner_Roll_no = int(input("Enter student roll no: "))

print("--- Fill your marks ---")
sub1 = eval(input("Bengali: "))
sub2 = eval(input("English: "))
sub3 = eval(input("Sanskrit: "))
sub4 = eval(input("History: "))
sub5 = eval(input("Computer Application: "))

total_Marks = sub1+sub2+sub3+sub4+sub5
total_percentage = (total_Marks / 500) * 100

if sub1>=24 and sub2>=24 and sub3 >= 24 and sub4 >= 24 and sub5 >= 21:
    if total_percentage >= int(90):
        grade = "A"
    elif total_percentage >= int(80):
        grade = "A+"
    elif total_percentage <= int(70):
        grade = "B"
    elif total_percentage <= int(60):
        grade = "B+"
    elif total_percentage <= int(50):
        grade = "C"
    elif total_percentage <= int(40):
        grade = "C+"
    elif total_percentage >= int(30):
        grade = "D"
    elif total_percentage < int(20):
        grade = "D+"
    print()
    print("----------------------------------")
    print("          Your Result             ")
    print("----------------------------------")
    print()
    print("Name:",Examiner_Name)
    print("Roll No:",Examiner_Roll_no)
    print("Total Marks:",total_Marks,"/ 500")
    print("Percentage:",int(total_percentage),"%")
    print("Status:","(PASS)")
    print("Grade:",grade)
    print()
else:
    print()
    print("----------------------------------")
    print("          Your Result             ")
    print("----------------------------------")
    print()
    print("Name:",Examiner_Name)
    print("Roll No:",Examiner_Roll_no)
    print("Total Marks:",total_Marks)
    print("Percentage:",int(total_percentage),"%")
    print("Status:","(FAIL)")
    print("Hey,",Examiner_Name,"contact your school because you are - FAIL")
    print("Grade:",grade)
    print()





