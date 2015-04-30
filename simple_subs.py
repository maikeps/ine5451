import sys
import string

def substitution_cypher_enc(text, key):
	cypher_text = "";
	uppercase_letters = list(string.ascii_uppercase)
	text = text.replace(' ', '')
	for letter in text:
		cypher_letter_pos = uppercase_letters.index(letter.upper())
		cypher_text += key[cypher_letter_pos].upper()
	return cypher_text

def substitution_cypher_dec(cypher, key):
	cypher = cypher.upper()
	key = key.upper()
	plain_text = "";
	uppercase_letters = list(string.ascii_uppercase)
	cypher = cypher.replace(' ', '')
	for letter in cypher:
		cypher_letter_pos = key.index(letter)
		plain_text += uppercase_letters[cypher_letter_pos].upper()
	return cypher_text

if len(sys.argv) < 3:
	print "Not enough parameters"
else:
	op = sys.argv[1]
	text = sys.argv[2]
	key = sys.argv[3]
	if op == '-e':
		print substitution_cypher_enc(text, key)
	elif op == '-d':
		print substitution_cypher_dec(text, key)