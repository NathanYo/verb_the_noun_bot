import tweepy, time, sys
 
argfile = str(sys.argv[1])
credential_arg = str(sys.argv[2])

credentials=open(credential_arg, 'r')
cred = credentials.readlines()
credentials.close()

CONSUMER_KEY = cred[0].rstrip('\n')
CONSUMER_SECRET = cred[1].rstrip('\n')
ACCESS_KEY = cred[2].rstrip('\n')
ACCESS_SECRET = cred[3].rstrip('\n')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()
    
for line in f:
    api.update_status(status=line)
    time.sleep(10800)#Tweet every 3 hours
