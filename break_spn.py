import spn

bits = {0:'0000', 1:'0001', 2:'0010', 3:'0011', 4:'0100', 5:'0101', 6:'0110', 7:'0111',\
	8:'1000', 9:'1001', 10:'1010', 11:'1011', 12:'1100', 13:'1101', 14:'1110', 15:'1111'}

key = '00111010100101001101011000111111'

def generate_input_xor(x):
	input_xor = {}
	for i in range(16):
		u = ''
		for j in range(4):
			u += spn.xor(x[j], bits[i][j])
			input_xor.update({bits[i]:u})
	return input_xor

def generate_output_xor(x_):
	output_xor = []
	u = ''
	tuplas = x_.items()
	for (key,value) in x_.items():
	#for i in range(len(tuplas)):
		y = spn.s[key]
		y_ = spn.s[value]
		
		aux = (y, y_)
		output_xor.append((key,value) + aux)
	# print(output_xor)

	return output_xor



def s_inverse():
	s = {}
	for (key, value) in spn.s.items():
		s.update({value:key})
	return s

def attack(tuples, s_inverse):
	keys_try = []
	keys_count = {}
	# print(tuples)
	for i in range(16):
		for j in range(16):
			keys_try.append((bits[i], bits[j]))
	
	for keys in keys_try:
		keys_count.update({keys:0})

	for tuple_ in tuples:

		if tuple_[2][0:4] == tuple_[3][0:4] and tuple_[2][8:12] == tuple_[3][8:12]:
			for key in keys_try:
				y2 = xor(key[0], tuple_[2][4:8])
				y4 = xor(key[1], tuple_[2][12:16])
				y2 = s_inverse[y2]
				y4 = s_inverse[y4]
				
				y2_ = xor(key[0], tuple_[3][4:8])
				y4_ = xor(key[1], tuple_[3][12:16])
				y2_ = s_inverse[y2_]
				y4_ = s_inverse[y4_]

				u2 = xor(y2, y2_)
				u4 = xor(y4, y4_)


				if u2 == '0110' and u4 == '0110':
					keys_count[key] += 1
	
	# print(keys_count)			

	max_ = -1
	max_key = ()
	for tuple_ in keys_try:
		if(keys_count[tuple_]) > max_:
			max_ = keys_count[tuple_]
			max_key = tuple_
	return max_key

def xor(bits1, bits2):
	xor = ''
	for i in range(len(bits1)):
		xor += spn.xor(bits1[i], bits2[i])
	return xor

def build_text(quadruples):
	tuples = []
	for quadruple in quadruples:
		for i in range(16):
			for j in range(16):
				bits1 = bits[i] + quadruple[0] + '0000' + bits[j]
				bits2 = bits[i] + quadruple[1] + '0000' + bits[j]
				tuples.append((bits1, bits2, spn.spn(bits1, key), spn.spn(bits2, key)))
	return tuples

quadruples = generate_output_xor(generate_input_xor('1011'))
print(attack(build_text(quadruples), s_inverse()))

