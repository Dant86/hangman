from nltk.corpus import words
from random import randrange

while True:
	response = ""
	index = randrange(len(words.words()))
	word = words.words()[index].lower()
	length = len(word)
	curr = (["_" for i in range(length)])
	print("The word has {} letters in it. Good luck!".format(length))
	amt_guesses = 10
	guessed = []
	while amt_guesses > 0:
		letter = ""
		while len(letter) != 1 or letter in guessed:
			letter = input("Guess a letter: ")
			if letter in guessed:
				print("Whoops! Looks like you already guessed that.")
		guessed.append(letter)
		if letter in word:
			for i in range(len(word)):
				if word[i] == letter:
					curr[i] = letter
			print("That's in the word!")
			print("Here's the word so far: {}".format("".join(curr)))
		else:
			print("Nope!")
			amt_guesses -= 1
		if "_" not in curr:
			if amt_guesses == 1:
				print("Awesome! You guessed the word with 1 try left!")
			else:
				print("Awesome! You guessed the word with {} tries left!".format(amt_guesses))
			break
	if amt_guesses == 0:
		print("Aw man! Looks like you lost.")
	print("The word was {}".format(word))
	while response != "yes" and response != "no":
		response = input("Play again? Please type \"yes\" or \"no\": ").lower()
	if response == "no":
		break
