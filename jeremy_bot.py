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
def maketweet(verblines, nounlines):
	verbNum = random.randrange(0,7785)
	nounNum = random.randrange(0,25271)
	verbChoice = verblines[verbNum].rstrip('\n')
	nounChoice = nounlines[nounNum].rstrip('\n')
	tweet = "%s The %s" % (verbChoice.title(), nounChoice.title())
	return tweet

def checktweet(tweetlines, tweet, i):
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
print tweet
tweets.write(tweet)
tweets.write('\n')
tweetarc.write(tweet)
tweetarc.write('\n')