s = {'0000':'1110', '0001':'0100', '0010':'1101', '0011':'0001', '0100':'0010', '0101':'1111', '0110':'1011', '0111':'1000',\
	'1000':'0011', '1001':'1010', '1010':'0110', '1011':'1100', '1100':'0101', '1101':'1001', '1110':'0000', '1111':'0111'}

p = {1:1, 2:5, 3:9, 4:13, 5:2, 6:6, 7:10, 8:14, 9:3, 10:7, 11:11, 12:15, 13:4, 14:8, 15:12, 16:16}

def spn(text, key):
	subkeys = generate_subkey(key)
	w = text
	for i in range(4):
		# w xor key
		u = ''
		for j in range(len(w)):
			u += xor(w[j], subkeys[i][j])
		#print('u', i+1, u)

		# caixa s
		half_bytes = ['']*4
		for j in range(0, len(u), 4):
			half_bytes[int(j/4)] = u[j:j+4]

		#aplicando a caixa s
		for j in range(len(half_bytes)):
			half_bytes[j] = s[half_bytes[j]]
		v = ''
		for j in range(len(half_bytes)):
			v += half_bytes[j]
		#print('v', i+1, v)

		# permut
		if(i < 3):
			w = ''
			for j in range(len(v)):
				w += v[p[j+1]-1]
			#print('w', i+1, w)

	y = ''
	for i in range(len(v)):
		y += xor(v[i], subkeys[4][i])

	return y

def generate_subkey(key):
	subkeys = [''] * 5
	for i in range(5):
		pos = 4*(i+1)-3
		subkey = ''
		for j in range(16):
			subkey += key[j+pos-1]
		subkeys[i] = subkey
	return subkeys

def xor(bit1, bit2):
	bit1 = int(bit1)
	bit2 = int(bit2)
	if bool(bit1) != bool(bit2):
		return '1'
	else:
		return '0'

print(spn('0010011010110111', '00111010100101001101011000111111'))