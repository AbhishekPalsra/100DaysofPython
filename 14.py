# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 =input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1.lower()
name2.lower()
score1=0
score2=0
combined_string=name2+name1
lower_string=combined_string.lower()  #need to store it somewhere
score1+=lower_string.count('t')
score1+=lower_string.count('r')
score1+=lower_string.count('u')
score1+=lower_string.count('e')
score2+=lower_string.count('l')
score2+=lower_string.count('o')
score2+=lower_string.count('v')
score2+=lower_string.count('e')




score=score1*10+score2
if score>90 or score<10:
    print(f"Your score is {score}, you go together like coke and mentos. ")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")






