import sys
import string

def simple_caesar_enc(text, key):
	cypher_text = "";
	uppercase_letters = list(string.ascii_uppercase)
	text = text.replace(' ', '')
	for letter in text:
		cypher_letter_pos = uppercase_letters.index(letter.upper())
		cypher_text += uppercase_letters[(cypher_letter_pos + key) % 26]
	return cypher_text

def simple_caesar_dec(cypher, key):
	return simple_caesar_enc(cypher, -key)

if len(sys.argv) < 3:
	print "Not enough parameters"
else:
	op = sys.argv[1]
	text = sys.argv[2]
	key = int(sys.argv[3])
	if op == '-e':
		print simple_caesar_enc(text, key)
	elif op == '-d':
		print simple_caesar_dec(text, key)