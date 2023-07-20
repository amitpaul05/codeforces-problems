print(ord('b'))

# print(chr(int(input("Enter a num :"))))

# calender
import calendar

cal = calendar.HTMLCalendar(firstweekday=6)
print(cal.formatmonth(2000, 4))

student_id = {input("Key : "): input("Value : ") for i in range(2)}
print(len(student_id))
print(sorted(student_id))
print(student_id)
for i in student_id:
    print(student_id[i])
