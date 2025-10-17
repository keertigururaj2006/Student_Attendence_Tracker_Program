classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

print(f"Attendance Percentage: {attendance_percentage:.2f}%")
