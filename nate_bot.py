import tweepy, time, sys

def read_file(argfile):
    '''This function reads all of the lines of a given file'''
    filename = open(argfile, 'r')
    f = filename.readlines()
    filename.close()
    return f

argfile = str(sys.argv[1]) # This is a list of tweets
credential_arg = str(sys.argv[2]) # This is the text file with access tokens

tweets_replied_to = "TWITTER TWEET IDS.txt" #TWITTER TWEET IDS.txt has a list of all tweets and DMs replied to

cred = read_file(credential_arg)

CONSUMER_KEY = cred[0].rstrip('\n')
CONSUMER_SECRET = cred[1].rstrip('\n')
ACCESS_TOKEN = cred[2].rstrip('\n')
ACCESS_SECRET = cred[3].rstrip('\n')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)



def delete_line(argfile, del_line):
    '''Rewrites the file without the parsed line'''
    filename = open(argfile, 'r+')
    f = filename.readlines()
    filename.seek(0) #Needs to select the very beginning to not write backwards
    for line in f:
        if line != del_line:
            filename.write(line)
    filename.truncate()
    filename.close()


def post_status():
    '''Allows a status to be posted whenever it is called'''
    f = read_file(argfile)
    try:
        api.update_status(status=f[0])
        delete_line(argfile, f[0])
    except tweepy.error.TweepError:
        print "ERROR: SENDING"

def get_search_mentions():
    '''Gets the last 100 mentions and checks if they have ever been replied to'''
    replied = read_file(tweets_replied_to)
    users = []
    mentions = api.mentions_timeline(count=100)
    for m in mentions: 
        tweet_id = str(m.id) + '\n'
        if tweet_id not in replied:
            users.append(m.user.screen_name)
            name = open(tweets_replied_to, 'a+')
            name.write(tweet_id)
            name.close()
    return users

def get_direct_messages():
    '''Gets the last 100 direct messages and checks if they've been replied to'''
    replied = read_file(tweets_replied_to)
    users = []
    direct_messages = api.direct_messages(count=100)
    for dm in direct_messages:
        message_id = str(dm.id) + '\n'
        if message_id not in replied:
            users.append(dm.sender.screen_name)
            name = open(tweets_replied_to, 'a+')
            name.write(message_id)
            name.close()
            print message_id
    return users

def post_replies():
    '''Posts all of the needed replies'''
    f = read_file(argfile)
    users = get_search_mentions()
    for i in users:
        tweet = "@%s %s" % (i, f[0])
        delete_line(argfile, f[0])
        try:
            api.update_status(status = tweet)
        except tweepy.error.TweepError:
            print "ERROR SENDING"

def post_direct_message():
    '''Posts all of the needed direct messages'''
    f = read_file(argfile)
    users = get_direct_messages()
    for i in users:
        message = f[0]
        delete_line(argfile, message)
        try:
            api.send_direct_message(screen_name = i, text = message)
        except tweepy.error.TweepError:
            print "ERROR SENDING"

def post(): #There's probably a cleaner way to do this...
    '''Contains the posting sequence.'''
    post_status()
    post_replies()
    post_direct_message()
    time.sleep(90)
    post_replies()
    post_direct_message()
    time.sleep(90)
    post_replies()
    post_direct_message()
    time.sleep(90)
    post_replies()
    post_direct_message()
    time.sleep(90)
    post_replies()
    post_direct_message()
    time.sleep(90)
    post_replies()
    post_direct_message()
    time.sleep(90)
    post_replies()
    post_direct_message()
    time.sleep(90)
    post_replies()
    post_direct_message()
    time.sleep(90)
    
def main():
    while True:
        post()

if __name__ == "__main__":
    main()
