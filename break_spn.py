import spn

bits = {0:'0000', 1:'0001', 2:'0010', 3:'0011', 4:'0100', 5:'0101', 6:'0110', 7:'0111',\
	8:'1000', 9:'1001', 10:'1010', 11:'1011', 12:'1100', 13:'1101', 14:'1110', 15:'1111'}

def generate_input_xor(x):
	input_xor = {}
	for i in range(16):
		u = ''
		for j in range(4):
			u += spn.xor(x[j], bits[i][j])
			input_xor.update({bits[i]:u})
	return input_xor

def generate_output_xor(x_, k):
	output_xor = []
	u = ''
	tuplas = x_.items()
	for i in range(len(tuplas)):

		y = spn.s[tuplas[i][0]]
		y_ = spn.s[tuplas[i][1]]
		
		aux = (y, y_)
		output_xor.append(tuplas[i] + aux)
	#print(output_xor)


generate_output_xor(generate_input_xor('1011'), 0)

def attack(T, s_):
	return 0
