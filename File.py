j = open("C:\\Users\\Lenovo\\OneDrive\\Documents\\NetBeansProjects\\Form\\Amit.text", mode='a')
try:
    words = input("What to write in the file : ")
    j.write(f"{words}\n")

finally:
    j.close()

f = open("C:\\Users\\Lenovo\\OneDrive\\Documents\\NetBeansProjects\\Form\\Amit.text", mode='r')
try:
    for line in f:
        print(line)

    print(f.tell())
finally:
    f.close()
