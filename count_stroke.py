# -*- coding: utf-8 -*- 
# Author: Yuan-Lu Chen <cheny@email.arizona.edu>
# The current program is inspired by Stephen Politzer-Ahles's perl scripts (see http://www.mypolyuweb.hk/~sjpolit/cgi-bin/strokecounter.pl)
# the fundamental data is from the unihan database (http://unicode.org/charts/unihan.html)


# set the default enconding to be 'utf-8'
import sys
reload(sys)  
sys.setdefaultencoding('UTF8') 

dex_to_stroke_number={}
with open('totalstrokes.txt','r') as d_to_s: 
	"""totalstrokes.txt is a table with the stroke count for every Unihan character created 
	by the Unihan database (http://www.unicode.org/charts/unihan.html). """
	for i in d_to_s:
		dex_to_stroke_number[i.split()[0]]=i.split()[1]

def char_to_dex(han_charater):
	#this function takes a charater as an input; return the hexadecimal utf-8 enconding. 
	#e.g. char_to_dex('fire') returns 706b
	out=repr(unicode(han_charater))
	return out[4:-1]

def char_to_stroke(han_charater):
	#this function puts char_to_dex and dex_to_stroke_number together; a char is coverted to dex, and then to stroke number
	try:
		return dex_to_stroke_number[char_to_dex(han_charater)]
	except:
		print 'Cannot find the stroke of {}!'.format(han_charater)	
		return 'ERR-'+han_charater

def sentence_to_stroke(sen):
	return ' '.join([char_to_stroke(i) for i in list(unicode(sen))])

def tokenize_sentence(text):
	'''
	A text is tokenize a text into sentences using non-han character as delimiter.
	e.g. 
	In [9]: tokenize_sentence('道德三皇五帝，功名夏后商周;')
	Out[9]: 
	[[u'\u9053', u'\u5fb7', u'\u4e09', u'\u7687', u'\u4e94', u'\u5e1d'],
 	[u'\u529f', u'\u540d', u'\u590f', u'\u540e', u'\u5546', u'\u5468']]
	
	'''
	out=[]
	temp=[]
	for i in list(unicode(text)):
		k=repr(i)[4:-1]
		if k in dex_to_stroke_number:
			temp.append(i)
		else:
			out.append(temp)
			temp=[]
	return out

if __name__ == "__main__":
	sentence="道德三皇五帝，功名夏后商周；abcd"
	print '''
    sentence_to_stroke(sentence) is the main function. Given a Chinese sentence,
    it return a sequence of number correspoding to the total stroke number of each charater in the sentence.
    
    Example:

    		In [12]: sentence= "道德三皇五帝，功名夏后商周；abcd"

		In [13]: sentence_to_stroke(sentence)
		Out[13]: {}

    	A non-han symbol is returned as "ERR-"the_symbol
    '''.format(sentence_to_stroke(sentence))