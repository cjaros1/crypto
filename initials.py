import string


def get_initials(fullname):
	initials=fullname[0]
	letter=""
	for i in range(1,len(fullname)):
		if (fullname[i] in string.ascii_lowercase or fullname[i] in string.ascii_uppercase) and (fullname[i-1] in string.punctuation or fullname[i-1]==" "):
			initials+=fullname[i]
	initials=initials.upper()
	return initials

def main():
	fullname=input("what is your name?\n")
	print(get_initials(fullname))
	return
	
if __name__=="__main__":
	main()
	