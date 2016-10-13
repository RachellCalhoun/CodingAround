# Decrypt string

# Here’s a simple strategy to encode a message: before each letter of the message, add a number and series of letters. The number should correspond to the number of letters that will precede the message's actual, meaningful letter.

# For example, the word “hey” could be coded with “0h2abe1zy”. To read the message, you would:

# skip 0, find the ‘h’
# skip 2 (‘a’ and ‘b’), find ‘e’
# skip 1 (‘z’), find ‘y’
# Write a function called “decode”, which takes a string in this code format and returns the decoded word. You may assume that coded strings are always legally encoded with this system.

# * Write your Decode

def decode(word):
    decoded_word = []
    for x in word:
        if x.isdigit():
            position = word.find(x)
            num_to_skip = int(x) + position + 1
            next_letter = word[num_to_skip]
            decoded_word.append(next_letter)
        else:
            pass
    return("".join(decoded_word))

decode("0h2abe1zy")
