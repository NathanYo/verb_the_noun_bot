from sys import argv
import random

script, vdict, ndict = argv
verbs = open(vdict)
verblines = verbs.readlines()
nouns = open(ndict)
nounlines = nouns.readlines()
tweetarc = open('TWEET_ARCHIVE.txt', 'a+')
tweetlines = tweetarc.readlines()
tweets = open('tweets.txt', 'a+')
"""opens the files needed and loads them into arrays"""
def maketweet(verblines, nounlines):
	"""function takes the arrays, picks a random line, strips the newline characters from them, and puts them in the form needed"""
	verbNum = random.randrange(0,7785)
	nounNum = random.randrange(0,25271)
	verbChoice = verblines[verbNum].rstrip('\n')
	nounChoice = nounlines[nounNum].rstrip('\n')
	tweet = "%s The %s" % (verbChoice.title(), nounChoice.title())
	return tweet

def checktweet(tweetlines, tweet, i):
	"""function takes the tweet generated from maketweet function and checks to see if it has previously been tweeted by comparing to TWEET_ARCHIVE"""
	for line in tweetlines:
		tweetcheck = tweetlines[i].rstrip('\n')
		if tweet == tweetcheck:
			return False
		i = i + 1
	return True		

tweeted = False
while tweeted == False:
	i = 0
	tweet = maketweet(verblines, nounlines)
	tweeted = checktweet(tweetlines, tweet, i)
	"""runs the functions until a tweet that has not been previously tweeted is made"""
print tweet
tweets.write(tweet)
tweets.write('\n')
tweetarc.write(tweet)
tweetarc.write('\n')
"""prints the tweet and appends it to tweets.txt and TWEET_ARCHIVE.txt"""