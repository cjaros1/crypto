import string
alphabet= string.ascii_lowercase
alphaUpper=string.ascii_uppercase

def alphabet_position(letter):
	letter=letter.lower()
	index=-1
	if letter in alphabet:
		index = alphabet.index(letter)            			
	return index	
	
def rotate_character(char,rot):
	rotChar=''	
	index=alphabet_position(char)
	if char in alphabet:
		rotChar=alphabet[(index+rot)%26]
	elif char in alphaUpper:
		rotChar=alphaUpper[(index+rot)%26]
	else:
		rotChar=char
	return rotChar
