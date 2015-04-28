import tweepy, time, sys
 
argfile = str(sys.argv[1])
credential_arg = str(sys.argv[2])

credentials = open(credential_arg, 'r')
cred = credentials.readlines()
credentials.close()

CONSUMER_KEY = cred[0].rstrip('\n')
CONSUMER_SECRET = cred[1].rstrip('\n')
ACCESS_TOKEN = cred[2].rstrip('\n')
ACCESS_SECRET = cred[3].rstrip('\n')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


filename = open(argfile,'r')
f = filename.readlines()
filename.close()

def post_status(f):
    for line in f:
        try:
            post_replies(f)
            api.update_status(status=line)
        except tweepy.error.TweepError:
            print "ERROR: Duplicate Tweet"
        time.sleep(30)#Tweet every 3 hours

def get_timeline():
    for status in tweepy.Cursor(api.user_timeline).items():
        print status

def get_search_mentions():
    users = []
    mentions = api.mentions_timeline(count=5)
    for m in mentions: 
        users.append(m.user.screen_name)
    return users


def post_replies(f):
    users = get_search_mentions()
    for i in users:
        tweet = "@%s %s" % (i, f[-1])
        try:
            api.update_status(status = tweet)
        except tweepy.error.TweepError:
            print "ERROR: Duplicate Tweet"

post_status(f)

#def main():
    #get_timeline()
#    print get_search_mentions()
#    post_replies(f)
#    post_status(f)

 #   if __name__ == "__main__":
 #       main()

