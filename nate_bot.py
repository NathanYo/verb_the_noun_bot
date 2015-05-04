import tweepy, time, sys

def read_file(argfile):
    filename = open(argfile, 'r')
    f = filename.readlines()
    filename.close()
    return f

argfile = str(sys.argv[1])
credential_arg = str(sys.argv[2])

tweets_replied_to = "TWITTER TWEET IDS.txt"

cred = read_file(credential_arg)

CONSUMER_KEY = cred[0].rstrip('\n')
CONSUMER_SECRET = cred[1].rstrip('\n')
ACCESS_TOKEN = cred[2].rstrip('\n')
ACCESS_SECRET = cred[3].rstrip('\n')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)



def delete_line(argfile, del_line):
    filename = open(argfile, 'r+')
    f = filename.readlines()
    filename.seek(0)
    for line in f:
        if line != del_line:
            filename.write(line)
    filename.truncate()
    filename.close()


def post_status():
    f = read_file(argfile)
    try:
        api.update_status(status=f[0])
        delete_line(argfile, f[0])
    except tweepy.error.TweepError:
        print "ERROR: Duplicate Tweet"

    #for line in f:
    #    try:
    #        api.update_status(status=line)
    #        delete_line(argfile, line)
    #    except tweepy.error.TweepError:
    #        print "ERROR: Duplicate Tweet"
    #    time.time.sleep(900) # Sleep for 10 minutes

def get_timeline():
    for status in tweepy.Cursor(api.user_timeline).items():
        print status

def get_search_mentions():
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


def post_replies():
    f = read_file(argfile)
    users = get_search_mentions()
    for i in users:
        tweet = "@%s %s" % (i, f[0])
        delete_line(argfile, f[0])
        try:
            api.update_status(status = tweet)
        except tweepy.error.TweepError:
            print "ERROR: Duplicate Tweet"

def post():
    post_status()
    post_replies()
    time.sleep(900)
    post_replies()
    time.sleep(900)
    post_replies()
    time.sleep(900)
    post_replies()
    time.sleep(900)
    post_replies()
    time.sleep(900)
    post_replies()
    time.sleep(900)
    post_replies()
    time.sleep(900)
    post_replies()
    time.sleep(900)
    post_replies()
    time.sleep(900)
    post_replies()
    time.sleep(900)
    post_replies()
    time.sleep(900)
    post_replies()
    time.sleep(900)

def main():
    post()

if __name__ == "__main__":
    main()
