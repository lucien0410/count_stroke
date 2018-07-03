'sentence_to_stroke(sentence)' is the main function. Given a Chinese sentence,
It returns a sequence of number corresponding to the total stroke number of each character in the sentence,
A non-han symbol is returned as "ERR-"the_symbol, and a error message is printed out. 

In a python shell, an example  is like:

	In [12]: sentence= "道德三皇五帝，功名夏后商周；abcd"

	In [13]: sentence_to_stroke(sentence)
	Cannot find the stroke of ，!
	Cannot find the stroke of ；!
	Cannot find the stroke of a!
	Cannot find the stroke of b!
	Cannot find the stroke of c!
	Cannot find the stroke of d!
	Out[13]: u'12 15 3 9 4 9 ERR-\uff0c 5 6 10 6 11 8 ERR-\uff1b ERR-a ERR-b ERR-c ERR-d'
