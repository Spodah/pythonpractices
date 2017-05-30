def xor_encrypt(text, key):
	text = text.upper()
	while(len(text) > len(key)):key = key + key
	return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(text,key)])
	
	
def xor_decrypt(secret_text, key):
	text = xor_encrypt(secret_text, key)
	return text
	
print(xor_encrypt('test', 'asde'))
