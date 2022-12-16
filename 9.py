print("Welcome to Tip Calculator")
t=float(input("What was the total bill? ")) # can do like this also
p=input("What percentage tip would you like to give? 10,12 or 15?")
n=input("number of persons")

tt= (float(t)+(int(p)*float(t))/100)/int(n)
rtt=round(tt,2) # round off to two dec places 33.6
print(rtt);
print(f"Each person should pay: {rtt:.2f}")

#python is little bit weried with floating point number