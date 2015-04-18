	
def isWordGuessed(secretWord, lettersGuessed):
	while True:
		for x in secretWord: 
			if x  in lettersGuessed:
				continue	
        	else:
				return False
				break
		return True

isWordGuessed('apple', ['a','b','s', 'l', 'p'])

def getGuessedWord(secretWord, lettersGuessed):
	guessedword = []
	finalguess = 0
	while True:
		for x in secretWord: 
			if x  in lettersGuessed:
				guessedword.append(x)
			if x not in lettersGuessed: 
        		
				guessedword.append("_ ")
							
		break
	finalguess = "".join(guessedword)
	
	return finalguess

print getGuessedWord("apple", ['b','s', 'l', 'p'])
