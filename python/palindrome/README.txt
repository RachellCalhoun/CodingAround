This program will take in a file or string and determine if it could be arranged into a palindrome.
User will be prompted for 'file' or 'text', user should enter accordingly.
If 'file' is chosen the user will be prompted to enter a filename.
If 'text' is chosen the user will be prompted to enter a text.
The file or text is checked for being a palindrome.
The outcome is either True or False.

Definition of palindrome used for this program (from https://en.wikipedia.org/wiki/Palindrome):
" A palindrome is a word, phrase, number, or other sequence
 of characters which reads the same backward or forward.
 Allowances may be made for adjustments to capital letters, punctuation, and word dividers."

This program checks for a palindrome considering only numbers and letters, lower or capital, but not special characters.

Input and output examples:

Text Examples:

Input: pali.has_palindrome()
Prompt: Please enter 'file'
or 'text' for what you'd like to test:
Input: text
Prompt: Enter a  string:
Input: "A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!"

Output: True

Input: pali.has_palindrome()
Prompt: Please enter 'file'
or 'text' for what you'd like to test:
Input: text
Prompt: Enter a  string:
Input: civci

Output: True

Input: pali.has_palindrome()
Prompt: Please enter 'file'
or 'text' for what you'd like to test:
Input: text
Prompt: Enter a  string:
Input: ivicc

Output: True

Input: pali.has_palindrome()
Prompt: Please enter 'file'
or 'text' for what you'd like to test:
Input: text
Prompt: Enter a  string:
Input: civil

Output: False

File examples:
* file use for this example (15,000+ characters) found here: http://norvig.com/pal1txt.html

pali.has_palindrome()
Please enter 'file'
or 'text' for what you'd like to test: file
Please enter a filename: long_pali.txt
Output: True



This program was written in response to the problem provided below:

"Write an efficient function has_palindrome that checks whether any permutation of an input string is a palindrome.

Examples:

has_palindrome('civic') should return True
has_palindrome('ivicc') should return True
has_palindrome('civil') should return False
Note, there is an O(n) solution to this problem.

Bonuses:

For bonus points, write a function that can read the text from a file."

