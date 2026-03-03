print("Welcome")

height = int(input("Enter height:: "))

if height>120:
    print("Okay")
    age = int(input("Enter age:: "))
    if age >=12:
        print("$5")
        bill = 5
    elif age>=18:
        print("$12")
        bill = 12
    else:
        print("$7")
        bill = 7
    want_photo = input("Want photo taken? ")

    if want_photo == "y":
        bill += 3
    
    print(f"You must pay {bill}")
else:
    print("No")