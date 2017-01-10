from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
	encrypted_msg=""
	key_index=0
	for i in range(len(text)):
		if text[i]==" " or not text[i].isalpha():
			encrypted_msg+=text[i]
		else:
			encrypted_msg+=rotate_character(text[i],alphabet_position(rot[key_index%len(rot)]))
			key_index+=1
	return encrypted_msg
	
def main():
	text=input("Type a message:\n")
	rot=input("Enter encryption key:\n")
	enc=encrypt(text,rot)
	print(enc)
	return
	

if __name__ == '__main__':
    main()
