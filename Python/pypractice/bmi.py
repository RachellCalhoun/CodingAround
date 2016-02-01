
input = raw_input("Enter your age")
input2 = raw_input("Enter BMI")
try:
    age = int(input)
    bmi = float(input2)
    if age < 0 or bmi < 0:
		print "try again"
		quit()
		
		#this will print if there is an error in input

except: 
    print " please enter a valid number"
    quit()
 

if bmi <= 22.0 and age <= 45:
    print "Low, eat something!!"
elif bmi <= 22.0 and age > 45 or bmi > 22.0 and age <= 45:
    print " Medium, be careful!"
elif bmi > 22.0 and age > 45: 
	print "high, go for a run!"	