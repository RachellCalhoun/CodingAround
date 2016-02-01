from random import * 

x = randint(1,100)

count = 0
higher = 100
lower = 1
attempts = 7

while count <= 7 :
    try:
        inputs = "Enter a number between " + str(lower) + " and " + str(higher) + " You have " + str(attempts) + " tries."
        input = raw_input(inputs)          
        n = int(input)
        
    except:
        print ("Invalid Entry")
        break    
        
    if x == n:
        print "You guessed the right number: ", x
        print "You guessed in", count, "attempts"
        break
    elif x < n:
        higher = n
        print "Guess lower"
    elif x > n:
        lower = n
        print "Guess higher"
    count += 1
    attempts -= 1
    
if count > 7:
    print ("You lost. The number was:"), x
else:
    print ("The number was:"), x   
     