class Key:
	def __init__(self, rotors, notches, ringstellung, plugboard, rotor_pos):
		self.rotors = rotors
		self.notches = notches
		self.ringstellung = ringstellung
		self.plugboard = plugboard
		self.rotor_pos = rotor_pos


class Enigma:
	# I = (AELTPHQXRU)(BKNW)(CMOY)(DFG)(IV)(JZ)(S)
	# II = (A)(BJ)(CDKLHUP)(ESZ)(FIXVYOMW)(GR)(NT)(Q)
	# III = (ABDHPEJT)(CFLVMZOYQIRWUKXSG)(N)
	# IV = (AEPLIYWCOXMRFZBSTGJQNH)(DV)(KU) 
	# V = (AVOLDRWFIUQ)(BZKSMNHYC)(EGTJPX) 
	rotor1 = {'a':'e', 'e':'l', 'l':'t', 't':'p', 'p':'h', 'h':'q', 'q':'x', 'x':'r', 'r':'u', 'u':'a', \
				'b':'k', 'k':'n', 'n':'w', 'w':'b', \
				'c':'m', 'm':'o', 'o':'y', 'y':'c', \
				'd':'f', 'f':'g', 'g':'d', \
				'i':'v', 'v':'i', \
				'j':'z', 'z':'j', \
				's':'s'}

	rotor2 = {'a':'a', \
				'b':'j', 'j':'b', \
				'c':'d', 'd':'k', 'k':'l', 'l':'h', 'h':'u', ' u':'p', 'p':'c', \
				'e':'s', 's':'z', \
				'f':'i', 'i':'x', 'x':'v', 'v':'y', 'y':'o', 'o':'m', 'm':'w', 'w':'f', \
				'g':'r', 'r':'g', \
				'n':'t', 't':'n', \
				'q':'q'}

	def enigma_enc(text, key):
		cypher = ""

		m1 = key.notches[0] - key.rotor_pos[0]
		nm2 = key.notches[1] - key.rotor_pos[1] - 1
		m2 = m1 + 26*nm2 + 1

		for j in range[0, len(text)]:
			k1 = (j - m1 + 26) / 26
			k2 = (j - m2 + 650) / 650

			i1 = p1 - r1 + 1
			i2 = p2 - r2 + k1 + k2
			i3 = p3 - r3 + k2

		return cypher

	def get_rotors(rotor_symbols):
		rotors = []
		for symbol in rotor_symbols:
			if symbol == "I":
				rotors.push(rotor1)
				break
			elif symbol == "II":
				rotors.push(rotor2)
				break
			elif symbol == "III":
				rotors.push(rotor3)
				break
			elif symbol == "IV":
				rotors.push(rotor4)
				break
			elif symbol == "V":
				rotors.push(rotor5)
				break
		return rotors

k = Key(["I", "II", "III"], ["a", "b", "c"], ["c", "d", "e"], {"a":"g"}, ["t", "w", "p"])
enigma = Enigma()