import sys
import string

def vigenere_enc(text, key):
	cipher_text = ""
	uppercase_letters = list(string.ascii_uppercase)
	text = text.replace(' ', '')
	i = 0
	for letter in text:
		cypher_letter_pos = uppercase_letters.index(letter.upper())
		key_letter_pos = uppercase_letters.index(key[i].upper())
		cipher_text += uppercase_letters[(cypher_letter_pos + key_letter_pos) % 26]
		i += 1
		if i >= len(key):
			i = 0

	return cipher_text

def vigenere_dec(cypher, key):
	plain_text = ""
	uppercase_letters = list(string.ascii_uppercase)
	cypher = cypher.replace(' ', '')
	i = 0
	for letter in cypher:
		cypher_letter_pos = uppercase_letters.index(letter.upper())
		key_letter_pos = uppercase_letters.index(key[i].upper())
		plain_text += uppercase_letters[(cypher_letter_pos - key_letter_pos) % 26]
		i += 1
		if i >= len(key):
			i = 0
	return plain_text

if len(sys.argv) < 3:
	print "Not enough parameters"
else:
	op = sys.argv[1]
	text = sys.argv[2]
	key = sys.argv[3]
	if op == '-e':
		print vigenere_enc(text, key)
	elif op == '-d':
		print vigenere_dec(text, key)