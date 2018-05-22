import os


def usr_str():
	print("Input a string that has multiple words.")
	print("Example: My name is Kyle")
	return input("--> ")


def reverse_order(usr_str):

	usr_str = usr_str.split(" ")
	rev = usr_str[::-1]

	joined = " ".join(rev)

	return joined


def main():
	play = True

	while play == True:

		usr_str_s = usr_str()
		print(reverse_order(usr_str_s))


		play_again = input('Do you want to enter another string? "Yes" or "No": ')

		if play_again == "yes":
			play = True
			os.system('clear')
		else:

			play = False

if __name__ == "__main__":
	main()
