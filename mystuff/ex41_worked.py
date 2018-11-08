import random
from urllib import urlopen
import sys
#import collections # for OrderedDict

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

#PHRASES = collections.OrderedDict() #added for keeping order

PHRASES = {
	"class %%%(%%%):":
	"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
	"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
	"Set *** to an instance of class %%%.",
	"***.***(@@@)":
	"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())


def convert(phrase): # have to rid empty lines in order to be able to paste into python teminal
	class_names = [w.capitalize() for w in
		random.sample(WORDS, snippets[0].count("%%%"))]
		#make the initial letter capitalized..
	other_names = random.sample(WORDS, snippets[0].count("***"))
	    #somehow the number could be pretty large, here 24
	results = []
	param_names = []
	for i in range(0, snippets[0].count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
	for sentence in phrase: #meaning as if sentence in snippet and if setence == phrase...
		result = phrase[:] 
	# fake class names
	for word in class_names:
		result = result.replace("%%%", word, 1)
	# fake other names
	for word in other_names:
		result = result.replace("***", word, 1)
	# fake parameter lists
	for word in param_names:
		result = result.replace("@@@", word, 1)
	results.append(result)
	return results


# keep going until they hit CTRL- D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)
		# since snippet has been initiated earlier, it has been set to be string..
		for snippet in snippets: #I see, it's looping through to the end
			phrase = snippets[0] #originally misspelled as PHRASES[snippet]
			answer = convert(phrase)
			if PHRASE_FIRST:
				question = answer

			print question

			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nBye"
	
	
for snippet in snippets:
	print snippet

