import re

class PermutationUtils:
	def permutation(self, char, steps, permutation):
		if char not in permutation:
			return char
		if steps < 0:
			permutation = self.inverse_permut(permutation)
			steps *= -1
		for i in range(steps):
			char = permutation[char]
		return char

	def inverse_permut(self, permutation):
		inverse = {}
		for (key, value) in permutation.items():
			inverse.update({value : key})
		return inverse

	def build_permutation(self, permutation):
		rotor = {}
		regex = re.compile('\((.*?)\)')
		permutations = regex.findall(permutation)
		for permutation in permutations:
			for i in range(len(permutation)):
				if i == len(permutation)-1:
					rotor.update({permutation[i] : permutation[0]})	
				else:
					rotor.update({permutation[i] : permutation[i+1]})
		return rotor

class Key:
	def __init__(self, rotors, notches, ringstellung, plugboard, rotor_pos):
		self.rotors = rotors
		self.notches = notches
		self.ringstellung = ringstellung
		self.plugboard = plugboard
		self.rotor_pos = rotor_pos


class Enigma:

	rotors = {}
	shift_up = {}
	reflector = {}
	plugboard = {}

	def __init__(self):
		self.permut = PermutationUtils()
		self.rotors.update({'I' : self.permut.build_permutation('(AELTPHQXRU)(BKNW)(CMOY)(DFG)(IV)(JZ)(S)')})
		self.rotors.update({'II' : self.permut.build_permutation('(A)(BJ)(CDKLHUP)(ESZ)(FIXVYOMW)(GR)(NT)(Q)')})
		self.rotors.update({'III' : self.permut.build_permutation('(ABDHPEJT)(CFLVMZOYQIRWUKXSG)(N)')})
		self.rotors.update({'IV' : self.permut.build_permutation('(AEPLIYWCOXMRFZBSTGJQNH)(DV)(KU) ')})
		self.rotors.update({'V' : self.permut.build_permutation('(AVOLDRWFIUQ)(BZKSMNHYC)(EGTJPX) ')})

		self.shift_up = self.permut.build_permutation('(ABCDEFGHIJKLMNOPQRSTUVWXYZ)')
		self.reflector = self.permut.build_permutation('(AY)(BR)(CU)(DH)(EQ)(FS)(GL)(IP)(JX)(KN)(MO)(TZ)(VW)')

	def enigma_enc(self, text, key):
		cypher = ""

		p1 = (ord(key.rotor_pos[0])-65)
		p2 = (ord(key.rotor_pos[1])-65)
		p3 = (ord(key.rotor_pos[2])-65)

		n1 = (ord(key.notches[0])-65)
		n2 = (ord(key.notches[1])-65)

		r1 = (ord(key.ringstellung[0])-65)
		r2 = (ord(key.ringstellung[1])-65)
		r3 = (ord(key.ringstellung[2])-65)

		m1 = n1 - p1
		nm2 = n2 - p2 - 1
		m2 = m1 + 26*nm2 + 1

		for j in range(len(text)):
			k1 = int((j - m1 + 26) / 26)
			k2 = int((j - m2 + 650) / 650)

			i1 = p1 - r1 + 1
			i2 = p2 - r2 + k1 + k2
			i3 = p3 - r3 + k2

			char = text[j]

			#plugboard
			char = self.permut.permutation(char, 1, key.plugboard)

			#rotor 1
			char = self.permut.permutation(char, i1+j, self.shift_up)
			char = self.permut.permutation(char, 1, self.rotors[key.rotors[0]])
			char = self.permut.permutation(char, -i1-j, self.shift_up)

			#rotor 2
			char = self.permut.permutation(char, i2, self.shift_up)
			char = self.permut.permutation(char, 1, self.rotors[key.rotors[1]])
			char = self.permut.permutation(char, -i2, self.shift_up)

			#rotor 3
			char = self.permut.permutation(char, i3, self.shift_up)
			char = self.permut.permutation(char, 1, self.rotors[key.rotors[2]])
			char = self.permut.permutation(char, -i3, self.shift_up)

			#reflector
			char = self.permut.permutation(char, 1, self.reflector)

			#rotor 3 back
			char = self.permut.permutation(char, i3, self.shift_up)
			char = self.permut.permutation(char, 1, self.permut.inverse_permut(self.rotors[key.rotors[2]]))
			char = self.permut.permutation(char, -i3, self.shift_up)

			#rotor 2 back
			char = self.permut.permutation(char, i2, self.shift_up)
			char = self.permut.permutation(char, 1, self.permut.inverse_permut(self.rotors[key.rotors[1]]))
			char = self.permut.permutation(char, -i2, self.shift_up)

			#rotor 2 back
			char = self.permut.permutation(char, i1+j, self.shift_up)
			char = self.permut.permutation(char, 1, self.permut.inverse_permut(self.rotors[key.rotors[0]]))
			char = self.permut.permutation(char, -i1-j, self.shift_up)

			#plugboard back
			char = self.permut.permutation(char, 1, key.plugboard)

			cypher += char

		return cypher


permut = PermutationUtils()

rotors = ["I", "II", "III"]
notches = ["Q", "E", "V"]
ringstellung = ["B", "B", "B"]
plugboard = permut.build_permutation('(AB)')
rotor_start_pos = ["A", "A", "A"]

k = Key(rotors, notches, ringstellung, plugboard, rotor_start_pos)
enigma = Enigma()
print(enigma.enigma_enc("BOCEJO", k))