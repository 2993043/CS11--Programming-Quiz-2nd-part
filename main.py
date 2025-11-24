#This is a calculator
#My name: Prithika Sathyan Poornima
#Who I collaborated with: Arianna Peguero, Jennifer Li
print("Welcome to the totally complicated calculator!")
solve = input("Do you want to solve an addition or subtraction problem?(add/subtract)")
if solve == "add" :
    num1 = int(input("What is the 1st value?"))
    num2 = int(input("What is the 2nd value?"))
    sum = (num1+num2)
    print("Your answer is: " + str(sum))
elif solve == "subtract":
    num1 = int(input("What is the 1st value?"))
    num2 = int(input("What is the 2nd value?"))
    difference = (num1-num2)
    print("Your answer is: " + str(difference))
else: 
    print("Please enter either addition or subtraction!")

