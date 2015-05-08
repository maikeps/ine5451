import urllib2
import string

response = urllib2.urlopen('http://www.inf.ufsc.br/~douglas.martins/')
html = response.read()

alphabet = {}
letters = string.ascii_lowercase
for letter in letters:
	alphabet.update({letter:0})

text = ''
for i in range(len(html)):
	character = html[i]
	if character == '<' and html[i+1] == 'p' and html[i+2] == '>': #achei <p>
		for j in range(i+3, len(html)):
			if character == '<' and html[j+1] == '/' and html[j+2] == 'p' and html[j+3] == '>': #achei <\p>
				i = i+j
				break
			text += html[j]


def remove_a(text):
	clear_text = ''
	for i in range(len(text)):
		if text[i] == '<':
			for j in range(i+1, len(text)):
				if text[j] == '>':
					i = i+j
					break
				clear_text += text[j]
		clear_text += text[i]
	return clear_text

print remove_a(text)