from sys import argv, exit
from helpers import rotate_character
	
def user_input_is_valid(cl_args):
	if len(cl_args)>1:
		if cl_args[1].isdigit():
			return True
		else:
			return False
	elif len(cl_args)==1:
		return False
	else:
		return False
	
def encrypt(msg,num):
	encrypted_msg=""
	for char in msg:
		encrypted_msg+=rotate_character(char,num)
	return encrypted_msg
	
def main():
	if len(argv)>1 and user_input_is_valid(argv):		
		num=int(argv[1])
	elif len(argv)==1:
		num=int(input("Rotate by:\n"))
	else:
		print("Error: invalid command line arguments:",argv)
		exit()
	msg=input("Type a message:\n")
	enc=encrypt(msg,num)
	print(enc)
	return
	
if __name__ == '__main__':
	main()
      