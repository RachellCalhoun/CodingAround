import string 

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    while True:
        for x in secretWord: 
            if x  in lettersGuessed:
                print "true"
                print x
                
            else:
                print "false"
                print "is breaking now"
                break
        print "it is a sucess"
        return True

isWordGuessed('apple', ['a','b','e','s', 'l', 'p'])

def getAvailableLetters(lettersGuessed):

    availableLetters = []
    for x in string.ascii_lowercase:
        if x in lettersGuessed:
            continue
        if x not in lettersGuessed:
            availableLetters.append(x)
        notGuessed = "".join(availableLetters)
        
        return notGuessed
print getAvailableLetters(['a', 'b', 'z'])