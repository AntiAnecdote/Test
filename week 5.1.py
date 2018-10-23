#Week 5
#Task 1.1
a = 13
b = 14
calculation = a + 1 <=b
calculation2 = a + 1 >=b
calculation3 = a + 1 !=b
print (calculation)
print (calculation2)
print (calculation3)
#Task 1.2
myage = input("How old are you : ")
print ("Hi there, You are " +myage+ " years old")
#Task 1.3
num1 = input("Enter the first number : ")
num2 = input("Enter the second number : ")
result = num1 + num2
print ("The result is " +result)
#Task 1.4
print ("average: %.2f" % ((3 + 11 + 78 + 112 + 4 + 18) / 6))
#Task 1.5
num1 = int(input ("Enter a number : "))
remainder = num1 % 7
print (remainder)
#Task 1.6
num1 = int(input ("Enter a number : "))
remainder = num1 % 7
print (remainder)
num2 = 7
num3 = num1 / num2
print (num3)
#Task 1.8
userinput = input("Enter Y to quit : ")
if userinput == 'Y':
    print ("Goodbye")
elif userinput == 'y':
    print ("Goodbye")
else:
    print ("Round 2 ~ Fight!")
#Task 1.9a
x = int(input ("Enter a number : "))
if (x) >0:
    print(x)
#Task 1.9b
if 1 + x > x ** sqrt(2) : y = y + x
#Task 1.9c
x = 1
y = 5
if x == 1:
    y += 1
print (x)
print (y)
#Task 1.9d
letterGrade = int(input("Enter your grade : "))
if letterGrade >= 90: print ("A")
elif letterGrade >= 80: print ("B")
elif letterGrade >= 70: print ("C")
elif letterGrade >= 60: print ("D")
elif letterGrade <= 40: print ("F")
#Task 1.10
richter = float(input ("Enter magnitude on richter scale : "))
if richter >= 8.0: print ("Most structures fall")
elif richter >= 7.0: print ("many buildings destroyed")
elif richter >= 6.0: print ("Many buildings considerbly damaged, some collapse")
elif richter >= 4.5: print ("Damage to poorly constructed buildings.")
elif richter <= 4.4: print ("No destruction of buildings.")
#Task 1.11
user = input("Enter a username : ")
print ("Welcome " + user + " Please select a password")
password = input("Enter a password : ")
count = 0


while count <= 4:
    if count == 4:
        print ("Access denied,Please press enter to exit and contact security to reset your password")
    elif (len(password)<8):
        input("Password needs to be more than 8 characters, Please try again : ")
    elif (len(password)>=8):
        print ("Password changed successfully")
        break
    
count += 1

#Task 1.12
for i in range(3):
    for j in range(1, 4):
        print (i + j, end="")
        print ()
        
#Task 1.13
        
for i in range (1,6):
    print("%d %d %d %d %d" % ((i**1),(i**2),(i**3),(i**4),(i**5)))



    
