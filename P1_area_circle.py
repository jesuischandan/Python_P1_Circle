#Basic program that calculate the area and circumference of circle!
while(True):
    print()
    print("This program will find the area and circumference of circle: ")
    print()
    consent = input("Do you want to use this Program (y/n): ")
    if consent == "n":
        break
    if consent == "y":
        print("To use this program, Please provide us the following details: ")
        print()
        nom = input("Enter your Last name: ")
        prenom = input("Enter your First name: ")
        email = input("Enter your E-mail Id: ")
        print("Thank you providing the details, let's go: ")
        print()
    try:
        r= int(input("Enter the Radius of circle: "))
        r = int(r)
        pi = 22/7
        area = pi*r*r
        cir = 2*pi*r
        print("the area of the circle is ",area,"sq. unit")
        print("the circumference of the circle is ",cir,"unit")
        print()
        consent = input("Do you want to restart this Program (y/n): ")
        if consent == "n":
            break
    except Exception as e:
        print("Exception occured: ",e)

print("Thank you using this program")
feedback = input("Please write your feedback here: ")
f = open("data.txt", "a")
f.write(str(nom))
f.write(", ")
f.write(str(prenom))
f.write(", ")
f.write(str(email))
f.write(", ")
f.write(str(feedback))
f.write("\n")
f.close()
