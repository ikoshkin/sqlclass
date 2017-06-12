# THIS IS GALVANIZE TECHICAL EXERCIZE SUBMISSION BY GOSHA KOSHKIN
# Q1.PY


# TEXT INPUT CAN BE DONE IN TWO MODE: TERMINAL LINE OR FILENAME
import string
from collections import defaultdict


def read_user_text(user_textfile = None):

	if (user_textfile != None):
		try:
			with open(user_textfile) as f:
				user_text = f.read()
				return user_text
		except IOError:
			print('Error: Wrong filename, try again')

	else:

		input_mode = input('Choose text input mode: 1 - command line / 2 - filename\n')

		if (str(input_mode) == '1'):
			user_text = input('Enter your text:\n')
			return user_text

		elif (str(input_mode) == '2'):
			user_textfile = input('Enter Text File Name:\n')
			try:
				with open(user_textfile) as f:
					user_text = f.readlines()
					return user_text
			except IOError:
				print('Error: Wrong filename, try again')

		else:
			print('Error: Wrong selection')
			return None

def clean_text(content):
	return str.lower(content.translate(
		str.maketrans("","", string.punctuation+'’‘-—()')))

def words_from_text(content):
	return content.split()

def word_freq(word_list):

	d = defaultdict(int)
	for word in words:
	    d[word] += 1
	return [k for k in sorted(d, key = d.get, reverse=True)]


if __name__ == '__main__':

    text_data = read_user_text('alice.txt')

    sentences = text_data.split(".")
    words = clean_text(text_data).split()
    unique_words = list(set(words))
    freq_word_list = word_freq(words)

    print("Total word count: ", len(words))
    print("Unique words: ", len(unique_words))
    print("Sentences: ", len(sentences))

    print("Brownies:")
    print("Average sentence length words", len(words)/len(sentences), "words")
    print("50 most frequesnt words: ", freq_word_list[:50])

