import sys


def vowelcount(s):
	total = 0
	for v in s: 
		if v == 'a'or v == 'i' or v == 'o' or v == 'u' or v == 'e' or v == 'A' or v == 'E' or v == 'I' or v == 'O' or v == 'U': 
			total += 1
	print "Number of Vowels: ", total


vowelcount("hello")
vowelcount("rachell")
vowelcount("Antartica")