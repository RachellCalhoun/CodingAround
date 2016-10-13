import re


def has_palindrome():
    stringfile = input('''Please enter 'file'
or 'text' for what you'd like to test: ''')
    if stringfile == "file":
        # try for valid filenames
        try:
            f = open(input("Please enter a filename: "), 'r')
            h = f.read()
            word_input = "".join(re.findall('[a-zA-Z0-9]+', h)).lower()
        # if filename not valid
        except:
            print("Your filename wasn't valid.")
            return False
        # check for empty file
        if word_input == "":
            print("Your file is empty.")
            return False
    elif stringfile == "text":
        # prompts for text
        word_input = input("Enter a  string: ").lower()
        # check for empty string
        if word_input == "":
            print("You didn't enter any text.")
            return False
    # if user didn't enter file or text
    else:
        print("Your entry wasn't valid. You should enter file or text.")
        return False
    odds = 0
    # get rid of all nonletter/number characters
    word = (re.sub("[^a-z0-9]+", "", word_input))
    for x in word:
        while x in word:
            # check how many multiples of each char
            multiples = word.count(x)
            # tracking odd multiples
            word = word.replace(x, "")
            # check for odd  multiples of each character
            if multiples % 2 != 0:
                # track each occurance of odd multiples
                odds += 1
            # if there is more than one odd occurance
            # of multiples it can't be a palindrome
                if odds > 1:
                    return False
        if word == "":
            break
    return True

