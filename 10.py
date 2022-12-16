print("Welcome to rollercoaster ride")
h=int(input("enter your height in cm : "))
#identation is very imp in case of python
if h>=120:
    print("you can rude rolleer coaster!")
    age=int(input("enter your age: "))
    if age<12:
        bill=5
        print("cost is 5 dollars.")
    elif age<15:
        bill=7
        print("cost is 7 dollars.")
    elif age<18:
        bill=10
        print("cost is 10 dollars")
    else:
        bill=12
        print("cost is 12 dollars")
    is_photo=input("do u want to click photos Y or N?")
    if is_photo=='Y':
        bill+=3

    print(f"total bill is {bill}.")






else:
    print("you are tooooo short")

