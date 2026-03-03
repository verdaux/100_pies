print("Welcome")

height = int(input("Enter height:: "))

if height>120:
    print("Okay")
    age = int(input("Enter age:: "))
    if age>=18:
        print("Pay $12")
    else:
        print("Pay $7")
else:
    print("No")