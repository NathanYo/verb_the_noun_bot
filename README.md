# verb_the_noun_bot
This is a twitter bot that uses a list of nouns and verbs and tweets out every few hours in the form of "Verb the Noun". It also responds to every tweet sent to it and every DM sent to it. It is built using tweepy on Python 2.7.

#How to use
This program uses the Tweepy library for Python. To install, just do
        
        pip install tweepy

# linear_search.py
This program performs a linear search through a list of verbs and nouns found at http://wordlist.aspell.net/12dicts/ which is the 2of12id.txt file. It writes all nouns to a noun text file, and all verbs to a verb text file. The usage of this script is:
        
        python linear_search.py <FILE_IN> <VERB_OUT> <NOUN_OUT>

# jeremy_bot.py
This program reads in a verb file, a noun file, and writes it to TWEET_ARCHIVE.txt and tweets.txt. The script only writes if the tweet does not exist in TWEET_ARCHIVE.txt. Usage:

        python jeremy_bot.py <VERB_IN> <NOUN_IN>
        
# nate_bot.py
This program does all of the tweepy usage. This script creates the bot that tweets, replies to tweets, and replies to direct messages. This script uses TWITTER TWEET IDS.txt to not spam people. This bot also needs a text file with the credentials of the twitter app. Usage:
        
        python nate_bot.py <TWEETS_OUT> <CREDENTIALS>
